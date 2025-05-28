# Raport - Przetwarzanie języka naturalnego w Pythonie

## 1. Wprowadzenie

Celem zadania było zapoznanie się z ogólnodostępnymi bibliotekami języka Python wykorzystywanymi w dziedzinie **przetwarzania języka naturalnego (NLP)**. Wybrane zostały trzy popularne i aktywnie rozwijane biblioteki.

- `nltk` - Natural Language Toolkit
- `spaCy`
- `transformers` (od Hugging Face)

---

## 2. Opis bibliotek

### 🔹 NLTK

- **Nazwa**: Natural Language Toolkit (NLTK)
- **Przeznaczenie**: Edukacyjne i klasycznne przetwarzanie języka - tokenizacja, stemming, tagging, parsowanie, analiza sentymentu
- **Główne funkcje*:
  - Tokenizacja tekstu
  - Analiza sentymentu (`SentimentIntensityAnalyzer`)
  - Operacje gramatyczne, np. tagowanie części mowy

🔗 [Dokumentacja NLTK](https://www.nltk.org/)  
🔗 [Repozytorium GitHub](https://github.com/nltk/nltk)

---

### 🔹 spaCy

- **Nazwa**: spaCy
- **Przeznaczenie**: Wydajne i nowoczesne NLP dla produkcyjnych zastosowań
- **Główne funkcje*:
  - Tokenizacja, lematyzacja
  - Rozpoznawanie nazw własnych (NER)
  - Dependency parsing
  - Obsługa wielu języków (z odpowiednimi modelami)

🔗 [Dokumentacja spaCy](https://spacy.io/)  
🔗 [Repozytorium GitHub](https://github.com/explosion/spaCy)

---

### 🔹 transformers
- **Nazwa**: transformers (Hugging Face)
- **Przeznaczenie**: Użycie zaawansowanych modeli językowych opartych na architekturze Transformer (np. BERT, GPT)
- **Główne funkcje*:
  - Analiza sentymentu
  - Klasyfikacja tekstu
  - Tłumaczenia, generacja tekstu, QA (pytanie-odpowiedź)
  - Łatwy dostęp do gotowych modeli przez `pipeline`

🔗 [Dokumentacja Transformers](https://huggingface.co/docs/transformers)  
🔗 [Repozytorium GitHub](https://github.com/huggingface/transformers)

---

## 3. Zalety i ograniczenia

### ✅ Zalety

| Biblioteka   | Zalety                                                                 |
|--------------|------------------------------------------------------------------------|
| `nltk`       | Dobra dokumentacja, świetna do nauki, wiele gotowych danych            |
| `spaCy`      | Szybkość działania, przejrzyste API, modele offline                    |
| `transformers` | Dostęp do nowoczesnych modeli (BERT, RoBERTa, GPT), proste `pipeline` |

---

### ⚠️ Ograniczenia

| Biblioteka   | Ograniczenia                                                           |
|--------------|------------------------------------------------------------------------|
| `nltk`       | Problemy z kompatybilnością danych (`punkt_tab`), starsza architektura |
| `spaCy`      | Duże modele językowe zajmują sporo miejsca                             |
| `transformers` | Wymaga internetu przy pobieraniu modeli, wyższe wymagania sprzętowe  |

---

## 4. Podsumowanie

Wszystkie trzy biblioteki nadają się do realizacji podstawowych i zaawansowanych zadań NLP. W ramach zadania przygotowano demonstracyjny skrypt `Zadanie.py`, który pokazuje praktyczme użycie każdej z nich. Projekt zrealizowano w środowisku **Visual Studio Code** przy użyciu **Python 3.11**.
