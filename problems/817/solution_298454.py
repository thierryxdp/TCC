def insere(lista_numero,n):
    '''Recebe uma lista com numeros em ordem crescente e 
    um numero inteiro n e retorna a lista de forma 
    crescente com o termo n na posição correta lugar'''
    x=lista_numero
    list.append(x,n)
    list.sort(x)
    return x

def maiores(lista_numero,n):
    ''' Recebe uma lista com numeros em ordem crescente e 
    um numero inteiro n e retorna a lista de forma 
    crescente com o os elementos maiores que o termo n '''
    x=insere(lista_numero,n)
    posicaoDeN=list.index(x,n)
    return x[posicaoDeN+1:]


def acima_da_media(notas_dos_alunos):
    '''Recebe as notas dos alunos 
    retorna uma lista na qual inclui apenas
    as notas maiores que a media dos alunos e organizada 
    de forma crescente'''
    notaMedia=sum(notas_dos_alunos)/len(notas_dos_alunos)
    listaNumerosMaiorIgualMedia=maiores(notas_dos_alunos,notaMedia)
    numerosIguaisAMedia=listaNumerosMaiorIgualMedia.count(notaMedia)
    listaComApenasAsNotasAcimaDaMedia=listaNumerosMaiorIgualMedia[numerosIguaisAMedia:]
    return listaComApenasAsNotasAcimaDaMedia