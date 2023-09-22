def posLetra(frase: str, letra: str, n: int) -> int:
    
    i = 0
    total = ''
    total2= ''
    
    if str.count(frase, letra) // n == 0:
        return -1
            
    while i < len(posLetra):
        total = total + frase[i]
        while str.count(total, letra) < n:
            total2 = total2 + total[i]
            
    return len(total2)