def insere(lista_numero,n):
    '''funcao que apos inserir uma lista e um numero n, ira retornar a lista inicial mais o numero n na sua posicao correta quando organizado crescentemente
    list, int -> list''' 
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista_numero,n):
    ''' funcao que dada um lista e um numero n, insere esse n na lista, organiza ela em ordem crescente e retira os valores menores que n
list, int -> list '''
    arruma = insere(lista_numero,n)
    achei = list.index(arruma,n)
    return arruma[achei+1:]

def acima_da_media(lista_numero):
    media = sum(lista_numero)/len(lista_numero)
    if media in lista_numero:
        list.remove(lista_numero,media)
    return maiores(lista_numero,media)