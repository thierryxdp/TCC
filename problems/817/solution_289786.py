def acima_da_media(notas):
    '''Função que dada uma lista(notas) com as notas dos alunos da turma, retorna uma lista ordenada com as notas que ficaram acima da média.
       parâmetro de entrada:list
       valor de retorno:list'''
    media=sum(notas)/len(notas)
    lista1=notas+[media]
    list.sort(lista1)
    p=list.index(lista1,media)
    c=list.count(lista1,media)
    return lista1[p+c:]