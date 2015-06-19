import re
import random
import itertools

from collections import defaultdict

PUNCTUATION = r"([\.\?\!\,\;\:])"
END_PUNCTUATION = r"([\.\?\!])"


class TextGenerator(object):
    """Generate text using Markov chain"""

    def __init__(self, context_size=1):
        """
        Constructor.

        context_size: how many words considered as context
        to choose the next one.
        """

        self.context_size = context_size
        self.chain = defaultdict(list)
        self.sentence_openings = []

    def _add(self, context, state):
        """Add a state in a context."""

        if type(context) == str:
            context = (context,)

        self.chain[context].append(state)

    def _get(self, context):
        """Get all possible states from a context."""

        if type(context) == str:
            context = (context,)

        return self.chain[context]

    def _next(self, context):
        """Choose randomically a state from a context."""

        return random.choice(self._get(context))

    def _to_text(self, result):
        """Transform the result tokens in a readable text."""

        def open_to_uppercase(pattern):
            return pattern.group(1) + " " + pattern.group(2).upper()

        text = " ".join(result)
        text = re.sub(" " + PUNCTUATION, r"\1", text)
        text = re.sub(END_PUNCTUATION + r" (.)", open_to_uppercase, text)
        text = re.sub(r"^" + END_PUNCTUATION + r" ", r"", text)

        return text

    def process_corpus(self, corpus):
        """Process a text to generate a Markov chain."""

        corpus = ". " + corpus
        corpus = re.sub(PUNCTUATION, r" \1", corpus)
        tokens = corpus.split()

        for i in range(len(tokens)-self.context_size):
            context = tuple(tokens[i:i+self.context_size])
            self._add(context, tokens[i+self.context_size])

            if re.match(END_PUNCTUATION, context[0]) is not None:
                self.sentence_openings.append(context)

    def generate_text(self, size):
        """
        Generate text after create a Markov Chain.

        size: number of sentences generated.
        """

        result = []
        result.extend(random.choice(self.sentence_openings))

        n_sentences = 0
        while n_sentences < size:
            try:
                new_word = self._next(tuple(result[-self.context_size:]))
                result.append(new_word)
            except IndexError:
                result.extend(random.choice(self.chain.keys()))

            if re.match(END_PUNCTUATION, new_word) is not None:
                n_sentences += 1

        return self._to_text(result)
