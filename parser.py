import nltk
import sys

# --- Ensure punkt + punkt_tab are available ---
for resource, path in [
    ("punkt", "tokenizers/punkt"),
    ("punkt_tab", "tokenizers/punkt_tab")
]:
    try:
        nltk.data.find(path)
    except LookupError:
        nltk.download(resource)

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NP VP | S Conj S

NP -> N | Det N | Det AdjP N | NP PP
AdjP -> Adj | Adj AdjP

VP -> V | V NP | V NP PP | V PP | V Adv | VP Adv | V NP Adv

PP -> P NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():
    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Lowercase everything and remove non-alphabetic tokens.
    """
    words = nltk.word_tokenize(sentence.lower())
    return [word for word in words if any(c.isalpha() for c in word)]


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is a subtree of the tree whose label is "NP"
    that does not itself contain any other NPs.
    """
    chunks = []
    for subtree in tree.subtrees(lambda t: t.label() == "NP"):
        if not any(child.label() == "NP" for child in subtree.subtrees(lambda t: t != subtree)):
            chunks.append(subtree)
    return chunks


if __name__ == "__main__":
    main()

