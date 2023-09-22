def retira_pontuacao(frase)
'''retorna sem pontuaçao'''
out = frase.translate(str.maketrans('', '',string.punctuation))
print(out)