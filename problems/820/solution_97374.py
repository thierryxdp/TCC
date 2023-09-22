def posLetra(frase: str, letra: str, n: int) -> int:
    
    i = 0
    total = ''
    total2= ''
    
    if str.count(frase, letra) // n == 0:
        return -1
            
    while i < len(frase):
        total = total + frase[i]
        
    while(total, letra) < n:
        total2 = total2 + total[i]
    i = i + 1
    return len(total2)