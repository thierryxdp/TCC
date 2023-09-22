def posLetra(frase,letra,pos):
    """função que determina a posição da letra conforme a ocorrencia
    str,str,int-> int"""
    txt = frase
    p=0
    i=0
    if txt.count(letra) < pos:
        return -1
    while i < len(frase) and p != pos:
        if frase[i] == letra:
            p = p+1
        i = i +1
    return i - 1