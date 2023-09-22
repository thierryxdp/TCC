def maiores (lista, n):
    '''Função que retorna, em ordem crescente, os números de uma 
    lista maiores que n
    list -> list'''
    lista_retorno = list.sort(lista)
    
    return [i for i in lista if i > n]

def acima_da_media (lista):
    '''Função que retorna as notas dos alunos em uma lista ordenada
    de notas acima da média'''
    
    return maiores