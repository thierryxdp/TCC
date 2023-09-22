# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """ A funcao concatena duas listas: lista1 e 
        lista 2, intercalando seus elementos;
        list, list -> list"""
    intercalada = []
    for a,b in zip(lista1, lista2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada