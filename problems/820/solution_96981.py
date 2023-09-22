def posLetra (palavra , letra , n):
    '''retorna a posicao da ocorrencia numero n da letra
    inserida no 2 arg
    str , str , int -> int'''
    
    i = 0
    j = 0
    
    if n == str.index(palavra,letra):
        return str.index(palavra,letra)
    
    if n > str.count(palavra,letra):
        return -1
    
    while i < len(palavra)-1:
        if letra == palavra[i]:
            j = j + 1
        elif j == n:
            return i - 1
        i = i + 1