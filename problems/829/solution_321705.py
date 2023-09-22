def soma_h(n):
    '''calcula o problema indicado na questao'''
    soma=0
    s=1
    while s<=n:
        soma+=1/s
        s+=1
    return round(soma,2)