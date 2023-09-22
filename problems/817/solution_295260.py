#Questão 5
def acima_da_media(lista):
    '''Retorna uma lista com apenas as notas acima da média da lista original
list -> list'''
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    primeiramaior=list.index(lista,media)+1
    return lista[primeiramaior:]