def posLetra(frase: str, letra: str, n: int) -> int:
    
    i = 0
    total = ''
    total2= ''
    
    if str.count(frase, letra) // n == 0:
        return -1
            
    while i < str.count(total, letra) + 1:
        total = total + frase[i]
        

        i = i + 1
    return len(total)