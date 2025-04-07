def detect_repetitions(text):
    nlp = spacy.load("de_core_news_lg")
    doc = nlp(text)

    repeated_phrases = set()

    for sent1 in doc.sents:
        if len(sent1) < 3:
            continue

        for sent2 in doc.sents:
            if len(sent2) < 3:
                continue

            if sent1.text != sent2.text and sent1.similarity(sent2) > 0.94:
                repeated_phrases.add(sent1.text)

    return repeated_phrases
