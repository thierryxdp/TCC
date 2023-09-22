def qtd_divisores (numero):
    '''Funcao que, dado um numero, retorna quantos divisores esse numero tem.
    int-> int'''
    
    lista = []
    
    for i in range(numero//2):
        if numero%i == 0:
            i = i
        lista.append(numero)
    return len (lista)