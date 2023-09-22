def posLetra(frase, l, o):
    """
    Essa função mostra em qual posição uma letra ('l') com a ocorrência ('o'),
    retorna a posição da frase na qual aquela ocorrência da letra se encontra.

    str,str,int => int
    """

    if frase.count(l) >= o:
        i = 0
        loc = []
        pos = list(frase)
        while i < len(pos) and len(loc)<o:
            if l == pos[i]:
                list.append(loc, pos[i])
            i = i + 1
        return i - 1
    else:
        return -1