def inverte(frase):
    """apos retirar a pontuaçao e transformar as letras maiusculas em minusculas, retorna o inverso da frase dada"""
    """str -> str"""
    
    frase = retira_pontuacao(frase)
    frase = str.lower(frase)
    l = str.split(frase)
    list.reverse(l)
    
    return str.join(" ",l)