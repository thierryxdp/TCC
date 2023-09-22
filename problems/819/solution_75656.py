def filtraMultiplos(*listan):
    '''Essa função filta os multiplos de um numero n,
    recebendo como entrada umaa lista de numeros e um numero,
    retornando uma outra lista com os elemtnos da lista original que 
    são divisiveis por n 
    list, float -> list'''
    valores_lista = listan[0]
    inteiro = listan[1]
    divisiveis = []
    contador = 0
    while contador < len(valores_lista):
        if valores_lista[contador] % inteiro == 0:
            divisiveis.append(valores_lista[contador])
        contador+=1
    return divisiveis