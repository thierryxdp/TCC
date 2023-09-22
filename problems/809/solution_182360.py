# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """
    Função recebe duas listas com tamanho 3. Organiza os elementos de forma pareada com 
    cada elemento de cada lista.
    Retorna uma lista.
    
    """
    lista=[]
    for k in range(len(lista1)):
        lista +=lista1[k],lista2[k]
    return lista