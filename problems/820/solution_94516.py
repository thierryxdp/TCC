def posLetra(f,s,n):
    """recebe como entrada uma frase "f",uma letra "s" e um número "n",sendo que o número indica a ocorrência desejada da letra (1 para a primeira,2 para a segunda,etc) e retorna em que posição da string aquela ocorrência da letra está,e caso exista menos ocorrências da letra que a ocorrência pedida,a função retorna o valor de -1"""
    i=0
    aparicoes=0
    if s not in f:
        return -1
    while aparicoes<n+1 and i<len(f):
        if s==f[i]:
            aparicoes=aparicoes+1
        i=i+1
    return i