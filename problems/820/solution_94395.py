def posLetra(f,s,n):
    """recebe como entrada uma string "s",uma letra "l" e um número "n",sendo que o número indica a ocorrência desejada da letra (1 para a primeira,2 para a segunda,etc) e retorna em que posição da string aquela ocorrência da letra está,e caso exista menos ocorrências da letra que a ocorrência pedida,a função retorna o valor de -1"""
    i=0
    ocorrencias=0
    while i<len(f) and ocorrencias<n+1:
        if f[i]==s:
            ocorrencias=ocorrencias+1
        i=i+1
    return i