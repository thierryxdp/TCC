# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """intercala elementos de duas listas de tamanho 3 cada
    inseridas como lista1 e lista 2 e retorna uma lista de 6 caracteres"""
    
    return lista1[0:1] + lista2[0:1] +lista1[1:2] +lista2[1:2] +lista1[2:3] +lista2[2:3]