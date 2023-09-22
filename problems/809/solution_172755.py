# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que intercala duas listas"""
    return [*sum(zip(lista1,lista2),())]