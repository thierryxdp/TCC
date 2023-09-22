#Exercício_06:
''' Essa função recebe um inteiro e devolve a soma de H. '''
''' int ---> float. '''

def soma_h(number):
    
    #Criando algumas variáveis e termos:
    i = 1 
    sum_of_numbers = 0
    
    #Criando o while:
    while i <= number:
        term = (1/i)
        sum_of_numbers += term
        i += 1
    return round(sum_of_numbers, 2)