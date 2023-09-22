def insere(lista_numero, n):
    '''
    Dada uma lista de numeros em ordem crescente, adiciona-se um numero nessa lista
    de forma que ela continue em ordem crescente.
    
    Entrada/Saida:
    list, float -> list
    '''
    lista_numero.append(n)
    return sorted(lista_numero)

def maiores(lista, n):
    lista = insere(lista, n)
    index = lista.index(n)
    return lista[index + 1:]