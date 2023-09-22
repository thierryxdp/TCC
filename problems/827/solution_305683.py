def qtd_divisores(numero):
    '''Função que recebe um numeo e calcula o numeros de divisores int-->int'''
    lista=[]
    for num in range (1,numero+1):
        if numero%num==0:
            lista.append(num)
            
    return len(lista)