def maiores2(lista,n):
    ''' '''
    if n not in lista:
        lista.append(n)
        lista.sort( )
        i = lista.index(n)
        return lista[i+1]
    else:
        lista.sort( )
        i = lista.index(n)
        return lista[i+1]
def acima_da_media(lista_notas):
    ''' Função que recebe uma lista de int's(lista_notas) contendo:
as notas dos alunos de uma turma;
e retorna outra lista ordenada contendo apenas as notas acima da média.
list-> list'''
    media = sum(lista_notas) / len(lista_notas)
    return maiores2(lista_notas, media)