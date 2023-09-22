def intercala(lista1, lista2):
    """Transforma duas listas de tamanho 3 gera outra lista que intercala os elementos um a um. List, list ->list"""
    	L3 = list()
        L2 = lista2
        L1 = lista1
        L3 = [L1[0]] + [L2[0]]
        L3 = L3 + [L1[1]] + [L2[1]]
        L3 = L3 + [L1[2]] + [L2[2]]
        return L3