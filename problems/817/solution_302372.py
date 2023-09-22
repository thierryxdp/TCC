#a funcao retorna uma lista ordenada com os alunos que ficaram acima da media 
#list->list
def acima_da_media(l):
    x= [n for n in l if n>(sum(l))/(len(l))]
    list.sort(x)
    return x