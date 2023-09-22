def maiores(lista_inteiros,n):
    '''funcao que retorna uma lista ordenada em ordem crescente apenas com
    numeros da lista de entrada que sejam maiores que o numero n
    list(int),int -> list(int)'''
    list.append(lista_inteiros,n)
    list.sort(lista_inteiros)
    indice_n = list.index(lista_inteiros,n)
    return lista_inteiros[indice_n+1:]

def acima_da_media(notas_alunos):
    '''funcao que retorna uma ista ordenada de ordem crescente
    apenas com as notas que ficaram acima da media, dada uma lista 
    de entrada com as notas totais.
    list(float) -> list(float)'''
    media = sum(notas_alunos)/len(notas_alunos)
    return maiores(notas_alunos,media)