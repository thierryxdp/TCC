def primo(n):
    '''Calcula e retorna se o número indicado(n) é primo ou não.
    int-->bool'''
    lista=[3,5,7,n]
    resto=n%2
    i=0
    resposta=True
    while resto!=0 and i<4:
        resto=n%lista[i]
        resposta=resto==0
        i=i+1
    return resposta