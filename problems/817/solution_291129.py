def maiores(lista,num):
    '''Escreva uma lista entre [] e um numero. A funcao retorna
    uma nova lista com os numeros maiores que o numero passado.
    list, int -> list'''
    lista.append(num) #adiciona o num no final da lista
    lista.sort() #ordena os numeros, do menor para o maior
    posicao=lista.index(num) #posicao de num na lista
    del lista[:posicao+1] #deleta todos os numeros da posicao 0 ate num (inclusive)
    while num in lista:
        lista.remove(num) #caso haja outros numeros igual a num, deleta todos
    return lista

def acima_da_media(lista):
    '''Escreva a nota dos alunos entre []. A funcao calcula
    a media da turma e da uma lista daqueles alunos que
    estao com a nota maior que essa media.
    list -> list'''
    media=sum(lista)/len(lista)
    acima_da_media=maiores(lista,media)
    return acima_da_media