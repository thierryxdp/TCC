def qtd_divisores (numero):
    '''Funcao que, dado um numero, retorna quantos divisores esse numero tem.
    int-> int'''
   
    contador = 0
    for divisor in range(1, numero+1):
        if numero%divisor == 0:
            contador+=1
    
    return contador