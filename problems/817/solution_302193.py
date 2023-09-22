def maiores(N,n):
   '''função em que dada uma lista de números inteiros e um
   número inteiro n, retorna outra lista, contendo todos os
   números da lista de origem com numeros maior que n, em ordem crescente;
   list,int -> list'''
   if n in N:
        list.sort(N)
        lista=list.index(N,n)
        return N[lista+1]
    else:
        list.append(N,n)
        list.sort(N)
        lista=list.index(N,n)
        return N[lista+1:]
    
def acima_da_media(lista):
        '''função que dada uma lista ordenada com as notas dos
        alunos de uma turma, retorne uma lista ordenada com as notas
        que ficaram acima da media; list -> list'''
        media_alu= (sum(lista))/(len(lista))
        return maiores(lista, media_alu)