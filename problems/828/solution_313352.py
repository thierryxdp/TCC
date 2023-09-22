def primo(n):
    '''Calcula e retorna se o número indicado(n) é primo ou não.
    int-->bool'''
    resposta=[False]
    for i in range(2,n) :
        resto=n%i
        if resto==0:
            resposta=resposta+[True]
        i=i+1
    return resposta not in [True]