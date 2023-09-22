''' retorna a frase inserida na função com suas pontuações substituidas
por espacos.

str --> str'''

def retira_pontuacao(frase):
    d = { '.': ' ', ':' : ' ', ';' : ' ', '-' : ' ', ',' : ' ', '?' : ' ', '!' : ' '}
    for c in d:
        frase =  str.replace(frase, c, d[c])
    return frase