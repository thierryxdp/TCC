def posLetra(string,letra,num):
    '''dada uma string, uma letra e um número, retorna a posição da string que aquela ocorrência da letra está;
    str, str, int --> int'''
    if num<=str.count(string,letra):
        prox=0
        while num-1>str.count(string,letra,0,prox):
            prox=prox+1
        return str.index(string,letra,prox)
    else:
        return -1