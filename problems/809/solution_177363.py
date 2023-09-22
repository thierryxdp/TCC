# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """a função retorna uma lista formada a partir da intercalação de elementos de duas listas,lista1 e lista2, gerando uma terceira lista"""
    x= (lista1[0],)+(lista2[0],)+(lista1[1],)+(lista2[1],)+(lista1[2],)+(lista2[2],)
    return x