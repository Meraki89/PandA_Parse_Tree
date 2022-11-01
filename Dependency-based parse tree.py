import nltk
from nltk import pos_tag, word_tokenize

# Example text
sample_text = "John hit the ball"

# Find all parts of speech in above sentence
tagged = pos_tag(word_tokenize(sample_text))
print(tagged)

# naive regular expression chunker that looks for tags beginning with letters that are characteristic of
# noun phrase tags (e.g. CD, DT, and JJ, NN, etc.)

grammar = r"""
              N: {<[CDJNP].*>+}
           """

cp = nltk.RegexpParser(grammar)
result = cp.parse(tagged)
print(result)
result.draw()

