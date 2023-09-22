# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """função que retorne duas listas L1 e L2 de tamanho 3 intercalando uma com a outra; str,str-> int, int, int, int, int, int"""
    L1= lista1[0:2:4:]
    L2= lista2[1:3:5:]
    L3= L1+L2
    return L3