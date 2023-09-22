def posLetra(frase: str, letra: str, n: int) -> int:
    
    i = -1
    total = ''
    total2= ''
    
    if str.count(frase, letra) // n == 0:
        return -1
            
    while n  > str.count(total, letra):
        if frase[i] in letra:
            total = total + frase[i]
        else:
            total = total + frase[i]
                
        i = i + 1
    return len(total)