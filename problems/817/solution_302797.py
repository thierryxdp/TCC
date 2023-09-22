def acima_da_media (lista):
    """Função que dada uma lista com notas, retorna apenas as notas acima da média.
    list-> list"""
lista_acima = []
if sum(lista)/len(lista) >= 5:
    return lista_acima