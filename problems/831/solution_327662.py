def lingua_p(P):
    '''Retorna uma palavra na lingua do P. str -> str'''
    PN = ''
    i=0
    consoantes= 'bBcCçÇdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ'
    while i<len(P):
        if P[i] not in consoantes:
            PN = PN + str.lower(P[i]+ 'P' + P[i])
            i=i+1
        elif P[i] in consoantes:
            PN = PN + str.lower(P[i])
            i=i+1
    return PN