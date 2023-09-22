def posLetra(frase: str, letra: str, n: int) -> int:
    """ recebe como entrada uma string, uma letra e um número 
    que indica a ocorrência desejada da letra, e retorna em que posição
    da string aquela ocorrência da letra, que ocorre 'n' vezes, está """
    
    i = 0
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
    return len(total) - 1