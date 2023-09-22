#Remova a pontuação da frase, usando a função anterior
def inverte(frase):
    """Função que dada uma frase retorna outra contendo as mesmas palavras
    da frase de entrada na ordem inversa, s/ letras maiúsculas, e s/ pontuação;
    str -> str
    """

    semPont = retira_pontuacao(frase)
    minusc = semPont.lower()
    removeEspacos = minusc.strip()
    novaFraseSplit = removeEspacos.split()[::-1]
    novaFraseJoin = " ".join(novaFraseSplit)
    return novaFraseJoin