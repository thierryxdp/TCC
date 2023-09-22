def filtraMultiplos(*listan):
    '''
    Dada uma lista de numeros e um numero, a 
    funçao retorna outra lista contendo todos
    os elemementos da lista original que forem divisíveis
    por n 
    list, int --> list
    '''
    valores_da_lista = listan[0]
    y = listan[1]
    div = []
    cont = 0
    while cont < len(valores_da_lista):
        if valores_da_lista[cont] % y == 0:
            div.append(valores_da_lista[cont])
        cont+=1
        return div