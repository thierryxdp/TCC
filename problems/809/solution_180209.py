# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que intercala duas listas, em ordem crescente, dada a lista 1 e a lista 2 com 3 elementos cada"""
    
    lista3 = lista1 + lista2
    
    sorted(lista3, key=int)