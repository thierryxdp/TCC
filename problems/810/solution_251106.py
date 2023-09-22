#Remova a pontuação da frase, usando a função anterior
def inverte(frase):
    """Função que dada uma frase retorna outra contendo as mesmas palavras
    da frase de entrada na ordem inversa, s/ letras maiúsculas, e s/ pontuação;
    str -> str
    """
    retira_pontuacao(frase)
    minusc = str.lower(frase)
    semPont = retira_pontuacao(minusc)
    listaFrase = str.split(semPont)
    listaInvertida = listafrase[::-1]
    str.join(' ', listaInvertida)
    return listaInvertida