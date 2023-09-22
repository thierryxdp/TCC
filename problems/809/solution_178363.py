# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que dadas duas listas 'lista1' e 'lista2' 
    gera uma lista L3 que é formada intercalando os elementos
    de lista1 e lista2"""
    
    n = len(lista1)
    interc = []
    
    for i in range(n):
        interc += lista1 [i], lista2 [i]
    return interc