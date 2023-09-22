def qtd_divisores(num):
    '''
       Função que recebe um numero (num) e retorna a
       quantidade de divisores que esse numero tem;
       int -> int
    '''
    divisores=[]
    numeros=list(range(num))
    numeros.append(num)
    numeros.remove(0)
    for i in numeros:
        if 10%i==0:
            divisores+=[i]
    return len(divisores)