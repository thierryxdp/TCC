def intercala(lista1, lista2):
    """Função que intercala duas listas e gera uma terceira lista com os elementos intercalados
    list,list -> list"""
    return (lista1 [0::] + lista2[1::])