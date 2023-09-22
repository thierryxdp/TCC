substitui(frase):
pontos = ['.',',','!','?','-',':',';']

frase = str.replace(frase, pontos, " ")

return frase

retira_pontuacao(frase):


frase = ''.join(map(substitui,frase))

return frase