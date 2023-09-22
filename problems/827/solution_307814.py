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
        if num%i==0:
            divisores+=[i]
        elif num<0:
            divisores=[0]
    return len(divisores)