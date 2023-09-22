def intercala(lista1, lista2):
    """Função que dada duas listas de tamanho 3 gera uma terceira lista
       que intercala os elementos da primeira lista e da segunda lista"""
    	lista3 = lista1 + lista2
        lista3 = lista1[0] + lista2[0] + lista1[1] + lista2[1] + lista1[2] + lista2[2]
        return lista3