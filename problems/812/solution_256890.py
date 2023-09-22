def retira_pontuacao(string):
    import string
transtable = str.maketrans('', '', string.punctuation)
clean_words = string.translate(transtable)
print(clean_words)