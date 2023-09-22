def lingua_p(palavra):
    traducao = ''
    for x in range(len(palavra)):
        if palavra[x] in 'qwrtypsdfghjklçzxcvbnmQWRTYPSDFGHJKLÇZXCVBNM':
            traducao = traducao + palavra[x]
        else:
            traducao = traducao + palavra[x] + 'p' + palavra[x]
    return traducao