# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """recebe duas listas com 3 elemenetos cada e retorna os valores delas intercalados
    list,list->list"""
    lista3 = [ ]
    lista3 = [lista1[0]] + [lista2[0]] + [lista1[1]] + [lista2[1]] + [lista1[2]] + [lista2[2]]
    return lista3