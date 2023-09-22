# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    
    if lista2[0]>lista1[0]:
        return list(lista1[0],lista2[0])
    
    
    
    elif lista2[0]<lista1[0]:
        return list(lista2[0], lista1[0])
    
    
    elif lista2[1]>lista1[1]:
        return list(lista1[1], lista2[1])
    
    elif lista2[1]<lista1[1]:
        return list(lista2[1], lista1[1])
    
    
    
    elif lista2[2]>lista1[2]:
        return list(lista1[2], lista2[2])
    
    elif lista2[2]<lista1[2]:
        return list(lista2[2], lista1[2])