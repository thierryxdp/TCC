def primo(n):
    '''Função que verifica se o número(n) é primo ou não
    retornando um valor booleano.
    int ->bool'''
    mensagem=()
    divisores=[]
    i=0
    for i in range(1,n+1):
        if n%i==0 and len(i)==2:
            mensagem='True'
        if n%i!=0 and len(i)>2:
            mensagem='False'
    return mensagem