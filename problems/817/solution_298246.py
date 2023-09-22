def insere(lista,n):
    list.append(lista,n)
    list.sort(lista)
    return lista

def maiores(lista,n):
    num=insere(lista,n)
    list.reverse(num)
    indice=list.index(num,n)
    list.reverse(num)
    return num[(indice)*-1:]

def acima_da_media(notas):
    num_alunos=len(notas)
    media=sum(notas)/num_alunos
    return maiores(notas,media)