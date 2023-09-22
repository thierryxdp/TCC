def posLetra(frase: str, letra: str, n: int) -> int:
    
    i = 0
    total = ''
    total2= ''
    
    if str.count(frase, letra) // n == 0:
        return -1
            
    while i < str.count(frase, letra):
        total = total + frase[i]
        

        i = i + 1
    return len(total)