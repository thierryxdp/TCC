def qtd_divisores(x):
    '''Função que calcula a quantidade de divisores que o 
    numero x possui.
    int ->int'''
    divisores=[]
    for i in range(1,x+1):
        if x%i==0:
            divisores=divisores+[i]
    return len(divisores)
def primo(n):
    '''Função que verifica se o número(n) é primo ou não
    retornando um valor booleano.
    int ->bool'''
    divisores=[]
    i=0
    for i in range(1,n+1):
        if n%i==0 or qtd_divisores(n)==2:
            mensagem=True           
        if n%i!=0 or qtd_divisores(n)>2:
            mensagem=False
    return mensagem