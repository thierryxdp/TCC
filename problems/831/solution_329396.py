def lingua_p(palavra):
    """traduz uma palavra para lingua do P;
    str->str"""
    novapalavra=''
    i=0
    while i<len(palavra):
        if palavra[i] not in 'aáéíóãôêeiouAÁÉÍÓÃÔÊEIOúÚU':
            novapalavra+=palavra[i]
        if palavra[i] in 'aáéíóãôêeioúÚuAÁÉÍÓÃÔÊEIOU':
            novapalavra+=palavra[i]+'p'+palavra[i]
        i+=1
    return novapalavra