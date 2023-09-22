def acima_da_media(notas):
    """ recebe uma lista de notas e retorna as notas que estiverem acima da média.
    list -> list
    Explicação: calcula primeiro a media fazendo o somatório e dividindo pela quantidade de notas, insere a média na lista das notas, ordena a lista, depois remove e compara, retornando os numeros maiores que a media.""""
   media= sum(notas)/len(notas)
   list.insert(notas,0,media)
   list.sort(notas)
   x=list.index(notas,media)
   if media in notas[x+1:]:
    int(media)
    notas.remove(media)
   return notas[x+1:]