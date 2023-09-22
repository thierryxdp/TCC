def qtd_divisores(numero):
    '''Função que calcula e retorna a quantidade de divisores de um número inteiro
    dado como entrada; int->int'''
    quantidade=0
    for i in range(1,numero+1):
        resto= numero%i
        if resto == 0:
            quantidade+=1
        else:
            quantidade = quantidade
    return quantidade

def primo(numero):
    '''Função que dado um número inteiro positivo como entrada, verifica se o mesmo é primo ou não.
    Essa função retorna TRUE caso o numero seja primo e FALSE caso contrário; int->bool'''
    if qtd_divisores(numero)== 2:
        return True
    else:
        return False