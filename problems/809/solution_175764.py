# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que intercala duas listas em um só"""
    intercalada = []
    for a,b in zip(lista1, lista2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada