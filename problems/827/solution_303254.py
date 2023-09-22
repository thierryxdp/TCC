def qtd_divisores(numero):
    '''Função que retorna a quantidade de divisores que um número(numero) passado como entrada possui.
       parâmetro de entrada:int
       valor de retorno:int'''
    lista=list(range(1,(numero+1)))
    resultado=[]
    for n in lista:
        if (numero % n) == 0:
            resultado=resultado+[n]
    return len(resultado)