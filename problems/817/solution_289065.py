def maiores(lista,n):
    """Função que recebe uma lista com numeros inteiros e um numero inteiro n e retorna uma lista com os numeros da lista original maiores que n;list,int->list"""
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)
    return lista[posicao+1:]

def acima_da_media(lista):
   """Função que recebe uma lista com notas de alunos e retorna uma lista apenas com as notas acima da média;list->list)"""
   media=sum(lista)/len(lista)
   return maiores(lista,media)