def lingua_p(p):
    '''dada uma palavra em portugês(p), retorna uma palavra traduzida
    para a língua do P com a palavra toda em minúscula;
    Ex: Caderno -> capadepernopo'''
    c = 0
    a = list(p)
    for i in a:
        if i in 'AEIOUaeiouÁáÉéÍíÓóÚúÃãÕõÂâÊêÎîÔôÛû':
            a[c] = i+'p'+i
        c = c + 1
    return str.join('',a)