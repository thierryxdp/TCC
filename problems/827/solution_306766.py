#Exercício_04:
''' Essa função recebe um número e retorna a quantidade de divisores que ele tem. '''
''' int ---> int. '''

def qtd_divisores(number):
    
    #Criando algumas variáveis e termos:
    i = 1
    dividers = 1

    #Criando o while:
    while i < number:
        division = number%i
        if division == 0:
            dividers += 1
        i += 1
    if number < 0:
        dividers = 0
    return dividers