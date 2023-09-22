def qtd_divisores(num):
    '''
       Função que recebe um numero (num) e retorna a
       quantidade de divisores que esse numero tem;
       int -> int
    '''
    numeros=list(range(num))
    numeros.append(num)
    numeros.remove(0)
    for i in numeros:
        divisores=[]
        if num%i==0:
            divisores+=[i]
    return len(divisores)