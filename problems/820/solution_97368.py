def posLetra(frase: str, letra: str, n: int) -> int:
    
    i = 0
    total = ''
    
    if str.count(frase, letra) // n == 0:
        return -1
            
    while i < len(posLetra):
        total = total + frase[i]
        while str.count(total, letra) < n:
            
    return total