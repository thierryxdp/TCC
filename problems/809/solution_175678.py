# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    lista3=[]
    for x in range(0,4):
    	lista3.append(lista1[x])
        lista3.append(lista2[x])
    
    return lista3