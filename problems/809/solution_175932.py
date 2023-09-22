# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1: list, lista2: list) -> list:
    """Essa função, dadas duas listas L1 e L2 como parâmetro de entrada,
    retorna uma nova lista formada pelos elementos de L1 e L2 intercalados"""
    
    L3 = []
    
    #Através da função Append, os elementos foram adicionados em suas respetivas posições na lista L3
    L3.append(lista1[0])
    L3.append(lista2[0])
    L3.append(lista1[1])
    L3.append(lista2[1])
    L3.append(lista1[2])
    L3.append(lista2[2])
    
    return L3