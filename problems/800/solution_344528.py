def total(lista, precos):
    soma = 0
    
    '''
    for x in lista: 
        soma = soma + precos[x]
    '''
    
    contador = 0
    while contador < len(lista):
        x = lista[contador]
        soma = soma + precos[x]
        contador = contador + 1
    
    return round(soma, 2)