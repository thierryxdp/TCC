def posLetra(frase: str, letra: str, n: int) -> int:
    
    i = 0
    total = ''
    total2= ''
    
    if str.count(frase, letra) // n == 0:
        return -1
            
    while n  > str.count(total, letra):
        if frase[n] in letra:
            total = total + frase[n]
        else:
            total = total + frase[n]
                
        i = i + 1
    return len(total)