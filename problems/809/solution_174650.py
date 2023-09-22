# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """função que intercala os elementos de duas listas lista1 e
    lista2 de tamanho 3 gerando uma lista3 entrada -> [int], [int]
    saida: [int]"""
    
    
    
    intercalada= []
    for a,b in zip(lista1, lista2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada