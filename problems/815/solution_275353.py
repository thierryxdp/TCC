#Função que recebe uma lista e um número, adiciona este número a lista
#e organiza ele em ordem crescente, retornando a nova lista organizada
#list, int -> list
def insere(lista_numero, n):
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero