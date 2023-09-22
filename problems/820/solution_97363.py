def posLetra(frase: str, letra: str, n: int) -> int:
    
    i = 0
    
    if str.count(frase, letra) // numero == 0:
        return -1
    
    while i < len(posLetra):
        if posLetra[i] == letra: