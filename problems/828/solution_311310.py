def primo(num):
    '''Função que dado um número inteiro positivo(num), verifica se o número é primo ou não, retornando True caso o número seja primo, ou False para o contrário.
       parâmetro de entrada:int
       valor de retorno:bool'''
    r=list(range(1,(num+1)))
    lista=[]
    for i in r:
        if (num%i)==0:
            lista=lista+[i]
    if len(lista)<=2:
        return True
    else:
        return False