def filtraMultiplos(*lista1):
    '''Essa função filta os multiplos de um numero n,
    recebendo como entrada umaa lista de numeros e um numero,
    retornando uma outra lista com os elemtnos da lista original que 
    são divisiveis por n 
    list, float -> list'''
    valores_lista = lista1[0]
    inteiros = lista1 [1]
    div = []
    cont = 0
    while cont < len(valores_lista):
        if valores_lista[cont] % inteiro == 0:
            div.append(valores_lista[cont])
            cont+=1
            return div