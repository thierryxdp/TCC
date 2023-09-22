def maiores(l1, n):
    '''
    	A função recebe uma lista numérica e um número inteiro n e retorna uma nova
        lista contendo todos os valores da lista anterior maiores que n, em ordem 
        crescente.
        n -> int
        l1 -> lista (contendo números)
    '''
    l1.append(n)
    l1.sort()
    an = l1.count(n)
    idn = l1.index(n)
    
    
    i = an+idn
    return l1[i:] 

def acima_da_media(notas):
    '''
    	A função recebe uma lista com as notas dos alunos de uma turma e retorna uma
        nova lista cotendo apenas as notas que ficaram acima da média, em ordem 
        crescente.
        notas -> list (notas dos alunos de uma turma)
        list -> list
    '''
    
    media = sum(notas)/len(notas)
    acima_da_media = maiores(notas, media)
    
    return acima_da_media