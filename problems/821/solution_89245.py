#Exercício_05:
''' Essa função recebe um número e devolve o seu fatorial. '''
''' int ---> int. '''

def  fatorial(number):
    
    resultado=1
    count=1

    while count <= number:
        resultado *= count
        count += 1
    return resultado