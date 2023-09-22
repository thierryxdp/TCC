def posLetra(s,l,n):
    '''Função que receb como entrad uma string, uma letra e um
    	número(ocorrência dessa letra desejada) e retorna a posição
        da string aquela ocorrência da lestra está, caso existam menos
        ocorrência da letra do que a ocorrência pedida, a função retorna
        -1
        
        str, str, int -> int'''
    i = 0
    r = 0
    while i < len(s):
        if s[i] == l:
            r = r + 1
            if r == n:
                return i
        i = i +1
    if r < n:
        return -1