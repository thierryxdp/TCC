def fatorial(num):
    '''Função que calcula o fatorial de um número; recebe
    como parâmetro um número dado pelo usuário; Int--> Int'''
    if(num>0):
        i=num
        resultado=1
        while i>0:
            resultado*=i
            i-=1
        return resultado