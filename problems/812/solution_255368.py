def retira_pontuacao(frase)
'''retorna sem pontuaçao'''
out = frase.translate(str.maketrans('', '', frase.punctuation))
print(out)