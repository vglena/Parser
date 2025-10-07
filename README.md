# 🧠 Sentence Parser (Context-Free Grammar with NLTK)

This project implements a **natural language parser** that uses a **context-free grammar (CFG)** to analyze and extract **noun phrase chunks** from English sentences.  

The parser leverages the **NLTK (Natural Language Toolkit)** library to tokenize, parse, and represent sentence structures as syntax trees.

---

## 🧩 Overview

The program reads English sentences from a text file (or user input) and performs the following steps:
 
1. **Preprocesses** the text (tokenization, lowercasing, and filtering non-alphabetic tokens).  
2. **Parses** the sentence using a context-free grammar defined by terminal and nonterminal rules.  
3. **Generates syntax trees** to represent the grammatical structure.  
4. **Extracts noun phrase (NP) chunks**, which are minimal noun phrases without nested NPs.  

Example output for the sentence:
`The detective in the armchair smiled.`

will include:
- A parse tree showing syntactic structure.  
- Extracted noun phrase chunks such as:
  - `the detective`
  - `the armchair`

---

## 📁 File Structure

```text
sentence-parser/
│
├── parser.py              # Core parser implementation (main logic)
├── sentences/             # Directory containing example text files
│   ├── 1.txt
│   ├── 2.txt
│   └── ...
│
├── README.md              # Documentation (this file)
├── requirements.txt       # Dependencies list
└── LICENSE                # MIT License
```
## ⚙️ Installation & Usage
1. Clone the Repository
```python
git clone https://github.com/yourusername/sentence-parser.git
cd sentence-parser
```
2. Install Dependencies
```python
pip install -r requirements.txt
```
3. Run the Parser
To parse a sentence file:
```python
python parser.py sentences/1.txt
```
Or, enter a sentence manually:
```python
python parser.py
Sentence: The detective in the armchair smiled.
```
## 🧩 Implementation Details
**Grammar Rules**
**TERMINALS** define the basic vocabulary (nouns, verbs, adjectives, etc.).
**NONTERMINALS** define how these components combine into valid grammatical structures.
You can extend or modify these rules in `parser.py` to handle new sentence patterns.
**Core Functions**
- `preprocess(sentence)`:
  Tokenizes and cleans input text.
- `np_chunk(tree)`:
  Extracts all minimal noun phrase chunks from a parse tree.

  ## 🧠 Example Output
```python
  $ python parser.py sentences/1.txt
Tree:
(S
  (NP (Det the) (N detective))
  (PP (P in) (NP (Det the) (N armchair)))
  (V smiled)
)

Noun Phrase Chunks:
- the detective
- the armchair
```

## 📦 Requirements

Your `requirements.txt` should include:
```text
nltk==3.9.1
```
## 🧾 License

This project is licensed under the MIT License — you’re free to use, modify, and distribute it with attribution.

## 💡 Notes
You can expand the grammar to support compound sentences, prepositional phrases, and conjunctions.
For advanced exploration, visualize parse trees using:
```python
tree.draw()
```


