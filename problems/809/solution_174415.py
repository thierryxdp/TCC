# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    nova_lista = [lista1[0],lista2[0],lista1[1],lista2[1],lista1[2],lista2[2]]
    return nova_lista
    #Usando o método zip
    # nova_lista = zip(lista1,lista2)
    # nova_lista = list(nova_lista)
    # vazia = []
    # for x in nova_lista:
    #     for y in x:
    #         vazia.append(y)
    # return vazia