# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """Função que recebe duas listas de tamanho 3 e gera outra lista intercalando os elementos da lista 1 e lista 2
    list, list -> list"""
    
    lista3 = lista1 + lista2
    lista3.sort()
    
    return lista3