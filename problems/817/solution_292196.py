def acima_da_media(notas):
    'função que recebe uma lista de notas retorna aquelas acima da media'
    media=sum(notas)/len(notas)
    list.sort(notas)