def maiores(lista, numero):
    list.append(lista, numero)
    list.sort(lista)
    index = lista.index(numero)
    origem = index+1
    nova_lista = lista[origem:]

    if len(nova_lista) == 1 and nova_lista[0] == numero:
        del nova_lista[0]
    
    return nova_lista

def acima_da_media(notas):
    media = sum(notas) / len(notas)
    acima = maiores(notas, media)
    return acima

notas1 = [6,4,7,2,9]
notas2 = [10,5,3,4]
notas3 = [7.3, 7.8,8,7,5.9,6.4]