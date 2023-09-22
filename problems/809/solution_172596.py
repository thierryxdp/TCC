def intercala(lista1, lista2):
    """Recebe duas listas de tamanho 3 e retorna uma terceira lista intercalando os elementos das duas listas; lista, lista -> lista"""
    return list(lista1[0])+list(lista2[0])+list(lista1[1])+list(lista2[1])+list(lista1[2])+list(lista2[2])