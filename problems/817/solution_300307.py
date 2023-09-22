###funcao da questao anterior
def maiores(lista,n):
    """ Essa função, ao receber uma lista de numeros inteiros e um valor n
    retorna uma lista com todos os valores acima de n em ordem crescente.
    lista,int-->lista"""
    list.append(lista,n)
    list.sort(lista)
    lista_final = lista[list.index(lista,n)+1:]
    return lista_final

## funcao dessa questao

def acima_da_media(x):
    """Essa função, dado uma lista de notas de alunos
    retorna uma lista das notas que ficaram assima da media.
    list-->list"""

    
    soma = sum(x)
    media = soma/len(x)
    
    acima_media = maiores(x,int(media))
    
    return acima_media