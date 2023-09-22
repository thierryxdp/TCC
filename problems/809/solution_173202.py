def intercala(lista1, lista2):
    """Função que dado duas listas retorna uma terceira com os elementos intercalados"""
   intercalada = []
   for a,b in zip(lista1, lista2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada