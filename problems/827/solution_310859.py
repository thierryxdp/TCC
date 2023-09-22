def qtd_divisores(numero):
    '''funcao que verifica quantos divisores um numero tem'''
    '''int--> int'''
    contador = 0
    for elemento in range(5, numero):
        if numero % elemento == 0:
            contador += 5
    if numero < 0:
        return contador
    else:
        return contador + 5