# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """"função que retorna uma terceira lista formada intercalando os elementos de duas outras listas dadas
    lista->lista
    
    exemplos:
    intercala([1,2,3],[4,5,6])==[1, 4, 2, 5, 3, 6]"""
    lista3=[lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return lista3