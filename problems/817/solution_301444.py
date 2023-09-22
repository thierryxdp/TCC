def maiores(lista, numero):
    list.append(lista, numero)
    list.sort(lista)
    index = lista.index(numero)
    nova_lista = lista[index+1:]
    
    return nova_lista

def acima_da_media(notas):
    soma = sum(notas) / len(notas)
    acima = maiores(notas, soma)
    return acima

notas1 = [6,4,7,2,9]
notas2 = [10,5,3,4]
notas3 = [7.3, 7.8,8,7,5.9,6.4]

acima_da_media(notas1)
acima_da_media(notas2)
acima_da_media(notas3)