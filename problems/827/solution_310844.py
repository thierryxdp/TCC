def qtd_divisores(numero):
    '''funcao verifica quantos divisores um numero qualquer tem.
    int--> int'''
    contador=0
    for elemento in range(1, numero):
        if numero % elemento == 0:
        contador += 1
    if numero < 0:
        return contador 
else:
    return contador + 1