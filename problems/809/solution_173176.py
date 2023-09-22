# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """caluclo e retorno de uma funcao que dada duas listas geram uma terceira intercalando elementos das listas de entrada"""
    lista3=((lista1[:1])+(lista2[:1])+(lista1[1:2])+(lista2[1:2])+(lista1[1+1:3])+(lista2[1+1:3])+(lista1[1+1+1:4])+(lista2[1+1+1:4])+(lista1[1+1+1+1:5])+(lista2[1+1+1+1:5])+(lista1[1+1+1+1+1:6])+(lista2[1+1+1+1+1:6]))
    return lista3