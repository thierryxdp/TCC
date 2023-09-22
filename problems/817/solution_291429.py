def acima_da_media(lista):
    '''Funcao que recebe uma lista com a as notas dos alunos e retorna a media e a as notas maiores que a media;
    list -> list'''
    media_notas = sum(lista)/len(lista)
    notas_maiores = []
    for maiores in lista:
        if maiores > media_notas:
            notas_maiores.append(maiores)
    return media_notas, sorted(notas_maiores)