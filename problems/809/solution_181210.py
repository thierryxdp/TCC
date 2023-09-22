# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """dada duas listas de tamanhos 3 gera uma terceira lista que e formada intercalando
    elementos da lista 1 e lista 2"""
    lista3=[]
    lista3.append(lista1[0])
    lista3.append(lista2[0])
    lista3.append(lista1[1])
    lista3.append(lista2[1])
    lista3.append(lista1[2])
    lista3.append(lista2[2])
    return lista3