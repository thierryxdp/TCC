def inverte(frase):
    """função que retorna a frase dada invertida, sem pontuação e sem letras maiúsculas
    str -> str"""
    nopont = retira_pontuacao(frase)
    minusculas = str.lower(nopont)
    lista = str.split(minusculas)
    listainvertida = lista[::-1]
    return str.join(' ',listainvertida)