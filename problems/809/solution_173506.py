# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def intercala(lista1, lista2):
    """funcao que intercala os elementos das listas lista 1 e da lista2
    fornecidas, ambas com 3 elementos, gerando uma lista3 
    
    list,list->list
    
    """
    a= list(lista1)
    b= list(lista2)

    return [a[0],b[0],a[1],b[1],a[2],b[2]]