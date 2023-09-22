def primo(numero):
    '''funcao que verifica se um número é primo;
    int -> bool'''
    i = 0
    for count in range(2,numero):
         if (numero % count == 0):
                i += i
               
             
    if i ==0:
        return True 
    else:
        return False