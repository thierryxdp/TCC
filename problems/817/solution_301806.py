def maiores(a,n):
    '''funçao que dada uma lista de tres numeros, e um outro numero,
    retorna outra lista que contem todos os numeros daa lista original
    maiores que n em ordem crescente'''
    '''list,int->list'''
    list.sort(a)
    lista=[]
    for i in a:
    	if i>n:
            lista.append(i)
    return lista

def acima_da_media(x):
    '''função que dada uma lista com as notas de alunos
    retorna outra lista ordenada com as notas que ficaram acima
    da media'''
    '''list->list'''
    media=sum(x)/len(x)
    return(maiores(x,media))