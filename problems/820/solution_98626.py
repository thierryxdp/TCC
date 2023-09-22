def posLetra(texto, letra, n):
    """ Dados um texto (texto), uma letra (letra) e um número (n), procura pela enésima ocorrência dessa letra no texto
    str, str, int -> int """
    for i in range(len(texto)):
        if texto[i]==letra:
            n-=1
            if n==0:
                return i
    return -1