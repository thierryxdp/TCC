def lingua_p(pal):
    '''Retorna a palavra inderida na lingua do P
    str --> str'''
    vog = ['a','e','i','o','u','á','à','ã','é','ê','í','ó','õ','ô','ú']
    i = 0
    pal = []
    for letr in pal:
        if letr in vog:
            list.append(pal, letr)
            list.append(pal, 'p')
            list.append(pal, letr)
        else:
            list.append(pal, let)
    return str.lower(str.join('',pal))