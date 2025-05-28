"""
Demonstracja bibliotek NLP: nltk, spaCy, transformers
Autor: Patrycja Dorszyńska
Opis:
- Tokenizacja i analiza sentymentu (nltk)
- Rozpoznawanie nazw własnych (NER) i lematyzacja (spaCy)
- Analiza sentymentu z modelem BERT (transformers)
"""


# === NLTK ===
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import TreebankWordTokenizer

nltk.download("punkt")
nltk.download("vader_lexicon")

text_nltk = "I absolutely love Python. It's so intuitive and powerful."

# Tokenizacja
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(text_nltk)
print(f"\n[NLTK] Tokeny: {tokens}")

#Analiza sentymentu
sia = SentimentIntensityAnalyzer()
sentiment_nltk = sia.polarity_scores(text_nltk)
print(f"\n[NLTK] Sentyment: {sentiment_nltk}")


# === spaCy ===
import spacy
nlp = spacy.load("en_core_web_sm")

text_spacy = "Elon Musk founded SpaceX and Tesla in the United States."
doc = nlp(text_spacy)

# Rozpoznawanie nazwanych jednostek
print("\n[spaCy] Rozpoznane jednostki:")
for ent in doc.ents:
    print(f"{ent.text} -> {ent.label_}")
    
# Lematyzacja
print("\n[spaCy] Lematy:")
for token in doc:
    print(f"{token.text} -> {token.lemma_}")


# === transformers (HuggingFace) ===
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
text_transformers = "I'm not sure if I liked the ending of the show."

result = classifier(text_transformers)
print(f"\n[transformers] Sentyment: {result}")
