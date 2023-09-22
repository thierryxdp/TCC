def posLetra(f,s,n):
    """recebe como entrada uma string "s",uma letra "l" e um número "n",sendo que o número indica a ocorrência desejada da letra (1 para a primeira,2 para a segunda,etc) e retorna em que posição da string aquela ocorrência da letra está,e caso exista menos ocorrências da letra que a ocorrência pedida,a função retorna o valor de -1"""
    l=list(f)
    if list.count(l,s)<n:
        return -1
    else:
        a=f.replace(s,"",n)
        b=a.index(s)
        return b