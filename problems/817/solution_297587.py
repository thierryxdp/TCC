def insere (lista_numero, n):
    '''dada uma lista ordenada(crescente) de numeros inteiros e um numero inteiro, retorna uma lista com o numero inteiro na
       posiçao correta.
       : list, int -> list
    '''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero

def maiores (lista_numero, n):
    '''dada uma lista de numeros inteiros e um numero inteiro n, retorna uma lista que contenha todos os números da lista 
       original maiores que n, em ordem crescente.
    '''
    n_ins = insere (lista_numero, n)
    n_ind = n_ins.index(n)
    n_lista = n_ins[n_ind+1:]
    return n_lista

def acima_da_media (notas):
    '''dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media
       : list -> list 
    '''
    media = sum(notas)//len(notas)
    Mmedia = maiores (notas, media)
    
    return Mmedia