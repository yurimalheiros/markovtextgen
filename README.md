Markov Text Generator
=====================

## How to use:

Import the module.

```
from textgen import TextGenerator
```

Create the generator, where *k* is the number of words considered as context.

```python
generator = TextGenerator(k)
```

Generate the text, where *n* is the number of sentences generated.

```python
generator.generate_text(n)
```

## Example

```python
from nltk.corpus import gutenberg
from textgen import TextGenerator

corpus = gutenberg.raw('shakespeare-hamlet.txt')

generator = TextGenerator(3)
generator.process_corpus(corpus)

print generator.generate_text(10)
```
