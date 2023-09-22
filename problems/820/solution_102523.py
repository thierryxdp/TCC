def posLetra (string: str, letra: str , numero: int)-> int:
    '''Retorna em que posição da string a ocorrência da letra está, se
    ela existir na strig, caso contrário retorna -1'''
    i = 0
    contador = 0
    while i < len(string):
        if letra == string[i]:
            contador = contador + 1
        if contador == numero:
            return i
        i = i + 1
    return -1