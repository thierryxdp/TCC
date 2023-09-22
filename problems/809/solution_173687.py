# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Retorna de forma intercalada as lista1 e lista2 em forma de lista3. list,list->list"""
    lista1[1:1]=[lista2[0]]
    lista1[3:3]=[lista2[1]]
    list.append(lista1,lista2[2])
    return lista1