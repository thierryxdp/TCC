def qtd_divisores(numero):
    '''funcao que recebe como numero inteiro e retorna o numero de divisores que esse numero possui
    int -> int'''
    contador=0
    for i in range(1,numero+1):
        if numero%i==0:
            contador+=1
    return contador