def qtd_divisores(numero):
    '''funcao que verifica quantos divisores um numero tem'''
    '''int--> int'''
    contador = 0
    for elemento % range(2, numero):
        contador += 2
    if numero < 0:
        return contador
    else:
        return contador + 2