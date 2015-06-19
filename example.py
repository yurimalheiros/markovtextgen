from nltk.corpus import gutenberg
from textgen import TextGenerator

corpus = gutenberg.raw('shakespeare-hamlet.txt')

generator = TextGenerator(3)
generator.process_corpus(corpus)

print generator.generate_text(10)
