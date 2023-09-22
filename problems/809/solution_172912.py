# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Tendo 2 listas de três elementos, intercala esses elemento gerando uma nova
    list,list->list"""
    return str.join(',',('[',str(lista1[0]), str(lista2[0]),str(lista1[1]),str(lista2[1]), str(lista1[2]),str(lista2[2]),']'))