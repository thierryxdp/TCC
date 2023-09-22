# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):  
    """ Função que intercala duas listas e gera um tereceira lista
    Entrada: lista
    Saída: lista """
    inter = lista1[0],lista2[0], lista1[1],lista2[1],lista1[2],lista2[2]
    return list(inter)