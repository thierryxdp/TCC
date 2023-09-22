def retira_pontuacao(s):
    punct = string.punctuation
for c in punct:
    s = s.replace(c, "")
print(s)