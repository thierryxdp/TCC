# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Dadas duas listas de tamanho 3, retornar uma terceira lista com os elementos das listas de entrada intercalados
    str->str"""
    lista3=[]
    lista3+=lista1[0]
    lista3+=lista2[0]
    lista3+=lista1[1]
    lista3+=lista2[1]
    lista3+=lista1[2]
    lista3+=lista2[2]
    return lista3