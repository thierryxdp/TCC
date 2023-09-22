#Remova a pontuação da frase, usando a função anterior
def inverte(frase):
    """Função que dada uma frase retorna outra contendo as mesmas palavras
    da frase de entrada na ordem inversa, s/ letras maiúsculas, e s/ pontuação;
    str -> str
    """
    sempont = retira_pontuacao(frase)
    minusc = str.lower(frase)
    listafrase = str.split(sempont)
    listainvertida = listafrase[::-1]
    str.join(' ',listainvertida)
    return listainvertida