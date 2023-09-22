def inverte(frase):
    """ função que dada uma frase retorne outra frase com as mesmas palavras só que na ordem inversa e sem a pontuação"""
x= str.lower(retira_pontuacao(frase))
y= str.split(x," ")
z= str.join(y," ")
return z[::-1]