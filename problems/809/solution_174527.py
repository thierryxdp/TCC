# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Recebe duas listas com 3 itens cada e retorna uma 
    terceira lista com os elementos de cada lista
    intercalados.
    list -> list"""
    return list((lista1[0],))+list((lista2[0],))+list((lista1[1],))+list((lista2[1],))+list((lista1[2],))+list((lista2[2],))