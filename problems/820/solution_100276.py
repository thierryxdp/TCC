def posLetra (frase, x, n):
    '''	
    	essa função recebe uma string, uma letra e um valor que indica a ocorrência da letra que
        se deseja e retorna em que posição da string a ocorrência da lestra está, se haver menos 
        ocorrências da Letra do que a solicitada, retorna "-1"
        str,str,int--> int
    '''
    if n > str.count(x,):
        return -1
    i = 0
    a = []
    while i<len(frase):
        if frase[i] == x:
            a.append(i)
        i = i+1
    return a[n-1]