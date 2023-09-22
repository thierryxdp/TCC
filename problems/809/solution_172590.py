# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    '''
    Dadas duas lista de tamanho 3, uma terceira é formada intercalando
    os elementos dessas listas.
    
    list, list -> list
    '''
    lista = []
    for i, j in lista1, lista2:
        lista += i
        lista += j
    return lista