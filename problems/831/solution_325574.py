def lingua_p(palavra):
    """ Dado uma palavra, a função retorna a a palavra traduzida na língua do p, ex: entao-> epentapaopo;
    str->str"""
    palavra=str.lower(palavra)
    palavra1=palavra[:]
    for i in range(len(palavra)):
        vogais=['a','e','i','o','u']
        if palavra[i] in vogais:
            list.remove(vogais,i)
            str.replace(palavra1,palavra[i],palavra[i]+p+palavra[i])
    return palavra1