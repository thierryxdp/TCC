#A função recebe uma lista ordenada e um número inteiro
#Insere o número na posição correta
def insere(lista_numero:list,n:int)->list:
    """A função recebe uma lista ordenada e um número inteiro
	   Insere o número na posição correta"""
    lista=lista_numero.append(int(n))
    list.sort(lista)
    return lista