#Ecercício_05:
''' Essa função recebe um número e retorna se ele é primo ou não. '''
''' int ---> bool. '''

def primo(number):
    
    #Criando algumas variáveis e termos:
    i = 2
    list_dividers = []
    list_comparison = []
    
    #Criando o while:
    while i < number:
        if number%i == 0:
            list_dividers += [i, ]
        i += 1
    
    #Criando o If para gerar o bool:
    if list_dividers == list_comparison:
        return True
    else:
        return False