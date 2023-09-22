#Função que dada uma frase como entrada, retorna uma outra frase que contem as mesmas palavras da frase de entrada,porém na ordem inversa,sem letras maiúsculas e sem a pontuação
def inverte(FraseFinal):
    listaA = str.lower(retira_pontuacao(FraseFinal))
    listaB = str.split(listaA)
    listaC= listaB[::-1]
    listaD = str.join(" ",(listaC))
    

    return listaD