def repetidos (lista):
    """Essa função irá receber uma lista e irá retornar o número de vezes que um elemento da lista é igual ao elemento anterior ; lista , int -> lista , int"""
    c = 0
    ListaNova = []
    while c < len (lista):
        if lista [c] == lista [c - 1] :
            ListaNova.append(1)
        c = c +1
	return len(ListaNova)