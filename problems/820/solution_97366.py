def posLetra(frase: str, letra: str, n: int) -> int:
    
    i = 0
    
    if str.count(frase, letra) // n == 0:
        return -1
            
    return str.count(frase, letra)