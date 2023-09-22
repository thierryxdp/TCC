def primo(numero):
    '''funcao que verifica se um dado 
    numero e primo
    entrada: inteiro
    saida: booleano
    '''
    divisores= []
    for divisor in range(1,(numero+1)):
        if numero%divisor==0:
            list.append(divisores, divisor)
            
    if divisores[0]==1 and divisores[1]==numero:
        return True
    if numero==1:
        return False  
    else: 
        return False