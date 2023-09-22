def lingua_p(palavra):
    """ Dado uma palavra, a função retorna a a palavra traduzida na língua do p, ex: entao-> epentapaopo;
    str->str"""
    palavra=str.lower(palavra)
    palavra1=palavra[:]
    vogais=['a','e','i','o','u','á','é','í','ó','ú','â','ê','î','ô','û','ã','õ']
    for i in range(len(palavra)):
        if palavra[i] in vogais:
            list.remove(vogais,palavra[i])
            palavra1=str.replace(palavra1,palavra[i],palavra[i]+'p'+palavra[i])
    return palavra1