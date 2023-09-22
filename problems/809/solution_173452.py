# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """A função intercala duas listas recebidas como parâmetros e retorna a nova lista gerada"""
    
    return [item for nova_lista in zip(lista1, lista2) for item in nova_lista]