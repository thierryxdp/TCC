def lingua_p(pal):
    '''Retorna a palavra inderida na lingua do P
    str --> str'''
    vog = ['a','e','i','o','u','á','à','ã','é','ê','í','ó','õ','ô','ú']
    i = 0
    pala= []
    for letr in pal:
        if letr in vog:
            list.append(pala letr)
            list.append(pala 'p')
            list.append(pala letr)
        else:
            list.append(pala let)
    return str.lower(str.join('',pala)