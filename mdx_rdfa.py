#!/usr/bin/env python

'''
RDFa Lite Extension for Python-Markdown
===========================================
Adds support for RDFa Lite annotations.

Dependencies
------------
* [Markdown 2.0+](http://www.freewisdom.org/projects/python-markdown/)

Copyright
---------
See LICENSE.md for details.
'''

import markdown
import re
from markdown.inlinepatterns import *
from markdown.treeprocessors import Treeprocessor

__version__ = "0.1"


def compile_re(pattern):
    return re.compile("^(.*?)%s(.*?)$" % pattern, re.DOTALL | re.X)

class RDFaExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        self.md = md

        # append to end of inline patterns
        md.inlinePatterns.add('rdfa_property', RDFaPropertyPattern( md), "<link")
        md.inlinePatterns.add('rdfa_link', RDFaLinkPattern(md), "<rdfa_property")
        md.inlinePatterns.add('rdfa_img', RDFaImagePattern(md), "<rdfa_link")
        md.treeprocessors.add('rdfa_block_attributes', RDFaTreeProcessor(md), '_end')

class RDFaLinkPattern(LinkPattern):

    pattern = r"""\(\s*(?P<property>[^)]+)\s*\)\s*\[(?P<label>[^\]]+)\]\s*\(\s*(?P<href>[^)]+)\s*\)"""
    
    def __init__(self, md=None):
        markdown.inlinepatterns.LinkPattern.__init__(self, self.pattern, md)

    def _clean_href(self, href):
        if href:
            if href[0] == "<":
                href = href[1:-1]
            return self.sanitize_url(self.unescape(href.strip()))
        else:
            return ""
        
    def handleMatch(self, m):
        """ Return a link element from the given match. """
        d = m.groupdict()

        el = markdown.util.etree.Element("a")
        el.set("property",d['property'])
        el.text = d['label'] if 'label' in d else ''
        if 'title' in d and d['title'] is not None:
            el.set('title', d['title'])
        el.set("href", self._clean_href(d['href'] if 'href' in d else None))

        return el

class RDFaTreeProcessor(Treeprocessor):

    pattern = re.compile(r"""(\(\s*((about\s+(?P<about>[^)]+))|(a\s+(?P<typeof>[^)]+))|(prefix\s+(?P<prefix>[^)]+))|(vocab\s+(?P<vocab>[^)]+)))\s*\))+""")
    
    def run(self, root):
        if root.text is not None:
            for m in self.pattern.finditer(root.text):
                for key, value in m.groupdict().items():
                    if value is not None:
                        root.set(key, value)
            root.text = self.pattern.sub('', root.text).strip()
        for child in root:
            self.run(child)
    
class RDFaImagePattern(RDFaLinkPattern):

    pattern = r"""!\(\s*(?P<property>[^)]+)\s*\)\s*\[(?P<title>[^\]]*)\]\s*\(\s*(?P<src>[^)]+)\s*\)"""
    
    def handleMatch(self, m):
        """ Return a link element from the given match. """
        d = m.groupdict()
        el = markdown.util.etree.Element("img")
        el.set("property",d['property'])
        if 'title' in d and d['title'] is not None:
            el.set('title', d['title'])
        el.set("src", self._clean_href(d['src'] if 'src' in d else None))

        return el


class RDFaPropertyPattern(Pattern):
    def __init__(self, md=None):
        markdown.inlinepatterns.Pattern.__init__(self, '', md)
        self.compiled_re = compile_re(r"""\((?P<property>[^)]+)\)\[(?P<content>[^\]]+)\]""")

    def getCompiledRegExp (self):
        return self.compiled_re

    def handleMatch(self, m):
        """ Returns etree """
        d = m.groupdict()
        element = markdown.util.etree.Element('span')
        element.text = d.get('content')
        element.set('property', d.get('property'))
        return element


def makeExtension(configs={}) :
    return RDFaExtension()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
