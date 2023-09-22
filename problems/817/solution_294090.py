def maiores(lista, n):
    if n not in lista:
        lista.append(n)
        lista.sort( )
        i = lista.index(n)
        sublista = lista[i+1:]
        repeticao = sublista.count(n)
def acima_da_media(notas):
    ''' Função que recebe uma lista de int's(lista_notas) contendo:
as notas dos alunos de uma turma;
e retorna outra lista ordenada contendo apenas as notas acima da média.
list-> list'''
    media = sum(notas) / len(notas)
    if media in notas:
        return maiores(notas, media)
    else:
        return maiores(notas, media)