def lingua_p(palavra):
    '''Essa função retorna uma palavra traduzida na lingua do p,
    str->str'''
    letra=list(palavra)
    for i in letra:
      cont=0
      for vogal in letra:
         if vogal in 'aeiouáéíóú' and letra[cont]==vogal:
           letra[cont]=letra[cont]+'p'+vogal
         cont+=1
    return str.join('',letra)