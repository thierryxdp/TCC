def qtd_divisores (numero):
    '''Funcao que, dado um numero, retorna quantos divisores esse numero tem.
    int-> int'''
    
    lista = []
    
    for i in range(1, numero//2):
        if numero % i == 0:
            i += 1
        lista.append(numero)
    return lista