# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que recebe duas listas de tamanho 3 e gera outra lista intercalando os elementos da lista 1 e lista 2
    list, list -> list"""
    
    
    list1 = lista1[0], lista2[0], lista[1]
    list2 = lista2[1], lista1[2], lista2[2]
    
    lista3 = list(list1) + list(list2)
    
    return lista3