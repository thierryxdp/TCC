def primo(n):
    '''Calcula e retorna se o número indicado(n) é primo ou não.
    int-->bool'''
    lista=range(3,n)
    resto=n%2
    i=0
    resposta=resto!=0
    while resposta==True and i<len(lista):
        resto=n%lista[i]
        resposta=resto!=0
        i=i+1
    return resposta