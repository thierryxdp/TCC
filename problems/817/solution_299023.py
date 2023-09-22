def acima_da_media(n:list):
    '''Recebe uma listagem com a nota(n) dos alunos, retornando
    uma lista ordenada com as notas que estão acima da 
    média'''
    media = sum(n)/len(n)
    notas=n.copy()
    notas.append(media)
    notas.sort()
    posicao=notas.index(media)
    maiores=notas[posicao+1:]
    if media in maiores:
        quantidade=maiores.count(media)
        maiores=maiores[quantidade:]
    return maiores