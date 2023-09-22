# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """retorna uma funcao que intercala os valores de duas listas
    sendo cada lista composta por apenas tres numeros
    int->list"""
    [x,y,z]=lista1
    [a,b,c]=lista2
    lista3=[lista1[0]]+[lista2[0]]+[lista1[1]]+[lista2[1]]+[lista1[2]]+[lista2[2]]
    return lista3