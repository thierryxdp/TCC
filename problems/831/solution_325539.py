def lingua_p(p):
    '''Função traduz um dada palavra para a lígua do P;
    str -> str'''
    trad=''
    for i in p:
        if i in 'aeiouãáàêéóõôúíAEIOUÃÁÀÊÉÓÕÔÚÍ':
            i= p[p.find(i)]+'p'+ p[p.find(i)]
        trad += i
    return trad