def qtd_divisores(numero):
    ''' Funcao que pega o numero de entrada e retorna a quantidade de divisores desse numero''' 
    tamanho= numero+1
    lista=[]
    for divisor in range(1,tamanho):
        if numero%divisor==0:
            lista.append(divisor)
    return len(lista)