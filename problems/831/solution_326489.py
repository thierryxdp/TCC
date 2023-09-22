def lingua_p(palavra):
    ''' '''
    for i in "aáeéiíoóuú":
      palavra = palavra.replace(i,i+'p')
    return palavra