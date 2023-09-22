# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Dados três parâmetros na lista1 e três parâmetros na lista2, a função irá
    intercalar o primeiro elemento da lista1 com o primeiro elemento da lista2
    e assim por diante. Recebe valores do tipo list e retorna um valor do tipo list """
    lista3 = [lista1[0], lista2[0], lista1[1], lista2[1], lista1[2], lista2[2]]
    return lista3