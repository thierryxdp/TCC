# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """função que intercala duas lista formando uma terceira com lementos l1 e l2
    entrada: lista1,lista 2:list
    saida:list"""
    return [lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]