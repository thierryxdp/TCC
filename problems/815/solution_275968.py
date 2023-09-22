def insere(lista_numero, n):
    """Função que dada uma lista não vazia como entrada que contém uma quantidade
    qualquer de valores númericos, retorna uma tupla cujo primeiro elemento é
    True caso a lista esteja ordenada e False, caso contrário e o segundo elemento
    indica se a  lista é crescente, decrescente ou desordenada; lista -> tupla"""

    listaA = lista[:]
    listaB = list.sort(lista)
    listaC = lista[:]
    lista2 = list.reverse(listaC) 
    
     if lista == listaA:
        return (True,'crescente')
    elif listaC == listaA:
        return (True,'decrescente')
    else:
        return (False,'desordenada')