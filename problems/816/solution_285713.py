def maiores(lista,n):
    'Função que retorna números ordenados de maneira crescente, dada uma lsita de números.'
    'list -> list'
    lista.append(n)
    lista.sort()
    comeco_nova_lista = lista.index(n)
    return lista[comeco_nova_lista+1:]