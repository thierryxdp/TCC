def primo(num):
    '''
       Função que recebe um numero inteiro e positivo (num)
       e retorna um booleano dizendo se esse numero é primo
       ou não;
       int -> bool
    '''
    divisores=[]
    numeros=list(range(num))
    numeros.append(num)
    numeros.remove(0)
    for i in numeros:
        if num%i==0:
            divisores+=[i]
    return len(divisores)==2