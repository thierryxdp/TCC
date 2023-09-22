def lingua_p(pala):
    '''Função que retorna uma mesma palavra traduzida
    para a língua do P.
    pala=str->str'''
    w=[]
    for l in pala:
        l=str.lower(l)
        if l in 'aeiouãâáàéêôõóúûíî':
            y=l+'p'+l
            list.append(w,y)
        else:
            list.append(w,l)
    return str.join('',w)