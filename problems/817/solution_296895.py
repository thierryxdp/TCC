def maiores(lista,n):
    '''Retorna uma lista em ordem crescente com os elementos
    maiores do que n; recebe como parâmetro uma lista e um
    número inteiro.List,Int-->List'''
    lista+=[n]
    list.sort(lista)
    pos_n=list.index(lista,n)
    return lista[pos_n+1:]
def acima_da_media(notas):
    '''Função que retorna uma lista apenas com as notas dos
    alunos que estão acima da média da instituição de ensino;
    recebe como parâmetro uma lista com as notas dada pelo
    usuário; List-->List'''
    media=sum(notas)/len(notas)
    return maiores(notas,media)