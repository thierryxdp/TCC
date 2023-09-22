def repetidos(lista):
    """retorna o numero de vezes que um elemento e igual ao elemento anterior. list -> int"""
    repeticao=0
    i=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            repeticao+=1
        i=i+1
    return repeticao