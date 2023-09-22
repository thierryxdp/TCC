def posLetra(frase,letra,n):
    """ essa função ia retornar em qual posição estara a ocorrencia dada pelo valor n, na frase. caso n tenha ocorrencia, irá retornar por -1
entrada -> str,str,int
saida -> int """
    i=0
    quantidade=[]
    while i<len(frase):
        if letra == frase[i]:
            quantidade = quantidade + [i,]
        i = i + 1
    if n in quantidade:
        quantidade = [0] + quantidade
        return quantidade[n]
    else:
        return -1