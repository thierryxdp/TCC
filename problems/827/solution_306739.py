def qtd_divisores(numero):
    '''função que verifica quantos divisores um
    número qualquer tem.
    int--> int'''

    contador = 1
    divisores = []

    for elemento in range(1, numero):
        if numero % elemento == 0:
            divisores.append(numero)
            
    if numero < 0:
        return len(divisores)
    else:
        return len(divisores) + 1