def primo (numero):
    '''Função que irá retornar se um número inteiro dado como entrada é 
    primo ou não
    int -> bool'''
    
    for contador in range (2, numero):
        if numero % contador == 0:
            primo =  False
            break
        else: 
            primo = True
      
    return primo