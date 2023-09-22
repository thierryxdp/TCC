# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """funçao que recebe duas listas e retorna a terceira
    lista que é formada pelos elementos das duas listas
    recebidas"""
    lista=lista1+lista2
    bless=lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]
    return list(bless)