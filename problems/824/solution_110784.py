def uppCons(f):
    """ Função que dada um frase como entrada, a mesma frase
        str->str"""
    
    i = 0
    fnova = ''
    
    while i < len(f):
         if frase[i] in "jdskgfkjsdagf":
            frasenova += str.upper(f[i])
        else:
            fnova += f[i]
        i += 1
    return fnova