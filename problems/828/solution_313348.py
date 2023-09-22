def primo(n):
    '''Calcula e retorna se o número indicado(n) é primo ou não.
    int-->bool'''
    resposta=[]
    for i in range(2,n) :
        resto=n%i
        resposta=resposta+[resto!=0]
        i=i+1
    return resposta in not [True]