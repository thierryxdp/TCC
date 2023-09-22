# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que recebe duas listas de tamanho 3 e gera uma terceira que intercala os elementos da primeira e da segunda. lista->lista"""
    lista3=[]
    lista3.append(lista1[0])
    lista3.append(lista2[0])
    lista3.append(lista1[1])
    lista3.append(lista2[1])
    lista3.append(lista1[2])
    lista3.append(lista2[2]) 
    return lista3