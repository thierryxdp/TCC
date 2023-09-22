def acima_da_media (nota):
    'Funcao que dada uma lista com as notas, retorna em ordem as notas que ficaram acima da media'
    'int+>int'
    soma=sum(nota)
    ni=len(nota)
    media=(soma//ni)
    list.append(nota,media)
    list.sort(nota)
    list.reverse(nota)
    i=list.index(nota,media)
    lista=nota[0:i]
    list.sort(lista)
      return lista