def soma_h(n):
    '''calcula o problema indicado na questao'''
    soma=0
    s=1
    while s<=n:
        soma+=1/s
        s+=1
    return round(soma,2)

def primo(n):
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True