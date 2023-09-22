def acima_da_media (lista_notas):
    '''Dada uma lista com as notas dos alunos de uma
       turma, retorne uma nova lista em ordem com as que
       ficaram acima da média;
       list -> list'''
    
    l1 = sum(lista_notas)
    l2 = len(lista_notas)
    med = l1/l2
    return l2
    lista = maiores(lista_notas,med)
    aux = list.count (lista,med)
    if aux>0 :
        return lista[aux: ]
    else: 
        return lista

def maiores (lista_N_Inteiros, numInt):
    
    novalista = ([i for i in lista_N_Inteiros if i > numInt])
    return sorted(novalista)