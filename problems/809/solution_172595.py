def intercala(lista1, lista2):
    """Recebe duas listas de tamanho 3 e retorna uma terceira lista intercalando os elementos das duas listas; lista, lista -> lista"""
    return list(lista1[0]+lista2[0]+lista1[1]+lista2[1]+lista1[2]+lista2[2])