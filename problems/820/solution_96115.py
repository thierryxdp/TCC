def posLetra(frase:str, letra:str, n:int) -> int:
    ''''''
    i = 0
    pos = -1
    while i < n:
        pos = frase.find(letra, pos+1)
        i = i+1
        
    return pos