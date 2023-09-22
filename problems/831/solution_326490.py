def lingua_p(palavra):
    ''' '''
    for i in "aáeéiíoóuú":
      palavra = str.replace(palavra,i,i+'p')
    return palavra