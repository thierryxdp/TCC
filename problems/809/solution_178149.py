def intercala(lista1, lista2):
"""recebe duas listas de tamanho 3 e retorna uma terceira lista que e 
    formada intercalando os elementos das duas primeiras
    list, list -> list"""
    
    l3 = [lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]]
    
    return l3