# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """
    função que retorna uma lista a partir de duas dadas como parâmetros
    list,list -> list
    
    Parâmetros:
    	lista1 e lista2
        
    Retorna
    	Lista com os elementos da lista1 e lista2 intercalados"""
    
    l1a = lista1[0]
    l2a = lista1[1]
    l3a = lista1[2]
    
    l1b = lista2[0]
    l2b = lista2[1]
    l3b = lista2[2]
    
    return [l1a,l1b,l2a,l2b,l3a,l3b]