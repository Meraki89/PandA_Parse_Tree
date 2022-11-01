import nltk
from nltk import pos_tag, word_tokenize


# Example text
sample_text = "John hit the ball"

# Find all parts of speech in above sentence
tagged = pos_tag(word_tokenize(sample_text))
# print(tagged)

grammar = r"""      
                 S: {<NP><VP>}               # Chunk NP, VP    
                NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
                PP: {<IN><NP>}               # Chunk prepositions followed by NP
                VP: {<VB.*><NP|PP|S>+$}      # Chunk verbs and their arguments
                VP: {<VB.*><NP>|<VP><PP>}
                VP: {<VB.*><NP>|<VP><PP>}
                PP: {<PRP.*><NP>}                
                """

cp = nltk.RegexpParser(grammar)
result = cp.parse(tagged)
print(result)
result.draw()
