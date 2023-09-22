def lingua_p(string):
    '''Função que calcula e retorna essa palavra na lingua do p.str->str'''
    nova = ""
    for elem in string:
        if elemento in "aeiouAEIOUáéíóú":
            nova = nova + elem+ "p" + elem
        else:
            nova = nova + elem
    return nova