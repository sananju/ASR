
"""
Code to compute different NLP metrics, as in Just et al., 2025:
DOI to follow.
Please cite the paper above if you use this code for your own work.
Authors: Sandra Just 10/07/2025
"""

import numpy as np
import spacy
from nltk.tokenize import sent_tokenize
from transformers import AutoTokenizer, AutoModel

#Load German spacy model
nlp = spacy.load("de_core_news_lg")

# Load the German BERT tokenizer and model
model_name_de = "bert-base-german-cased"
model_de = AutoModel.from_pretrained(model_name_de)
tokenizer_de = AutoTokenizer.from_pretrained(model_name_de)

#Total tokens
def get_text_tokens(text, stopwords=[]):
    doc = nlp(text)
    return [token.lemma_.lower() for token in doc if ((token.text and token.lemma_ and token.lemma_ != ' '
                                                      and token.pos_ not in ['PUNCT', 'NUM']))]

#Total sentences
sentences = sent_tokenize(transcript)
num_sentences = len(sentences)

#local coherence
def cos_sim(v1, v2):
    return np.inner(v1, v2)/(np.linalg.norm(v1)*np.linalg.norm(v2))

def get_local_coherence(clause_vectors):
    if len(clause_vectors) <= 1:
        return [np.nan]
    local_coherence_list = []
    for i in range(len(clause_vectors)-1):
        local_coherence_list.append(cos_sim(clause_vectors[i], clause_vectors[i+1]))
    return local_coherence_list
