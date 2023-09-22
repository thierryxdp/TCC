def maiores(lista,n):
    'Função que retorna números ordenados de maneira crescente, dada uma lsita de números.'
    'list -> list'
    if not n in lista:
    	lista.append(n)
    lista.sort()
    comeco_nova_lista = lista.index(n)
    return lista[comeco_nova_lista+1:]

def acima_da_media(lista):
    'Função que calcula o número de notas de alunos acima da média, dadas as notas e número de notas.'
    media = sum(lista)/len(lista)
    return maiores(lista,media)