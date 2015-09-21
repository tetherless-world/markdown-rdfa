# RDFa Lite for Markdown
A Python Markdown extension that lets authors embed RDFa Lite in markdown documents rendered to HTML. RDFa Lite is a simple way to add facts about things that you talk about on your web pages.

Here's a simple (but complete) example of the sorts of RDFa annotations you can use in markdown-rdfa:

```markdown
(vocab http://schema.org/)
(prefix ov: htttp://open.vocab.org/terms/)
(about #manu)(a Person)
My name is (name)[Manu Sporny] and you can give me a ring via (telephone)[1-800-555-0199].
(url)[my homepage](http://manu.sporny.org/),
!(image)[](http://manu.sporny.org/images/manu.png)
My favorite animal is the (ov:preferredAnimal)[Liger].
```

This example compiles to the canonical example from the [RDFa Lite primer](http://www.w3.org/TR/rdfa-lite/):

```html
<p vocab="http://schema.org/" prefix="ov: http://open.vocab.org/terms/" resource="#manu" typeof="Person">
My name is
<span property="name">Manu Sporny</span>
and you can give me a ring via
<span property="telephone">1-800-555-0199</span>.
<a href="http://manu.sporny.org/" property="url">my homepage</a>,
<img property="image" src="http://manu.sporny.org/images/manu.png" />
My favorite animal is the <span property="ov:preferredAnimal">Liger</span>.
</p>
```

Note that it is possible to generate invalid RDFa simply by including literals where there should be URIs or CURIEs, improperly formatting a prefix element, or not declaring a prefix before using it. Today, this is on the honor system, partly because markdown can be embedded in a surrounding HTML that would address some of these issues by declaring prefixes, setting vocabularies, etc. 

# Installation

To install via pip, use the following command:

```
pip install git+git://github.com/tetherless-world/markdown-rdfa.git#egg=markdown-rdfa
```

# Using the extension

There are detailed instructions at the python markdown site, but to run markdown-rdfa on a document from the command line, simply try this:

```
python -m markdown -x rdfa example.rmd
```

example.rmd is an example markdown-rdfa document.
