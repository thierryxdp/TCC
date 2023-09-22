# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''recebe e retorna uma lista em que os elementos são os elementos das outras 2 listas intercalados
    list, list -> list'''
    return list(lista1["0"] + lista2["0"] + lista1["1"] + lista2[1] + lista1[2] + lista2[2])