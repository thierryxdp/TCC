def insere(lista_numero,n):
    '''dada uma lista de numeros em ordem crescente e dado
    um numero inteiro n, é retornado a lista de forma 
    crescente com o termo n em seu devido lugar'''
    x=lista_numero
    list.sort(x)
    list.append(x,n)
    list.sort(x)
    return x

def maiores(lista_numero,n):
    '''dado uma lista de numeros inteiros e um numero n;
    temos como volta uma lista que contem apenas os numeros
    maiores que n, ademais com a sua ordem crescente de termos'''
    x=insere(lista_numero,n)
    posicaoDeN=list.index(x,n)
    return x[posicaoDeN+1:]

def acima_da_media(notas_dos_alunos):
    notaMedia=sum(notas_dos_alunos)/len(notas_dos_alunos)
    x=maiores(notas_dos_alunos,notaMedia)
    return x