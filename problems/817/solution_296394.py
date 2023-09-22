def maiores(inteiros, n):
    
    ''' Função que, dada uma lista de números
        inteiros e um número inteiro (n), retorna
        uma lista contendo os números da lista
        original que são maiores que n, em 
        ordem crescente.
        list, int -> list '''
    
    inteiros.sort()
    
    if n in inteiros:
        inteiros = inteiros[inteiros.index(n):]
    
    if n not in inteiros:
        inteiros.append(n)
        inteiros.sort()
        inteiros = inteiros[inteiros.index(n):]
        
    return inteiros


def acima_da_media(notas):
    
    ''' Função que, dada uma lista com as notas
        dos alunos de uma turma, retorna uma lista
        ordenada com as notas que ficaram acima
        da média.
        list -> list '''
    
    lista_notas = maiores(notas, sum(notas)/len(notas))
    
    return lista_notas