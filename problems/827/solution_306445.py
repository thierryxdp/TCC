ddef qtd_divisores(num):
    '''Program aque lê um número inteiro n e retorna quantidade de numeros dividisores de n
    int -> int'''
    if num > 0:
        l=[]
        for i in range(1, num//2+1):
            if num % i == 0:
                list.append(l,i)        
        return len(l)+1
    if num <= 0:
        return 0