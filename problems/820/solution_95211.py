def posLetra(frase,letra,num):
    """
    Dada uma frase e uma letra, o numero diz qual a ocorrencia dessa
    letra na frase (ex: se num = 3, trata-se da terceira vez que 'letra'
    aparece) e retorna-se a posicao na string em que essa ocorrencia se
    encontra
    string, string, int -> int
    """
    i = 0
    n = []
    c = frase.count(letra)
    if c < num:
        return -1
    while i<len(frase) and len(n)<num:
        if frase[i] == letra:
            n = n + [i]
        i = i + 1
    return n[num]