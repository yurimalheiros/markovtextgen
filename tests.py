from textgen import TextGenerator


def test_add_item():
    generator = TextGenerator()
    generator._add("x", "a")

    assert generator._get("x")[0] == "a"


def test_add_two_items():
    generator = TextGenerator()
    generator._add("x", "a")
    generator._add("x", "b")

    assert generator._get("x")[0] == "a"
    assert generator._get("x")[1] == "b"


def test_process_corpus():
    corpus = "this is a test. this is only an example."

    generator = TextGenerator()
    generator.process_corpus(corpus)

    assert generator._get("this")[0] == "is"
    assert generator._get("this")[1] == "is"

    assert generator._get("is")[0] == "a"
    assert generator._get("is")[1] == "only"


def test_process_corpus_k2():
    corpus = "this is a test. this is only an example."

    generator = TextGenerator(2)
    generator.process_corpus(corpus)

    assert generator._get(("this", "is"))[0] == "a"
    assert generator._get(("this", "is"))[1] == "only"

    assert generator._get(("is", "a"))[0] == "test"
    assert generator._get(("is", "only"))[0] == "an"
