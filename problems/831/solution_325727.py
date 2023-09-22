def lingua_p(palavra):
    "função que recebe uma palavra e retorna essa mesma palavra traduzida para a língua P.str->str."
    traducao = ''
    for x in range(len(palavra)):
        if palavra[x] in 'qwrtypsdfghjklçzxcvbnmQWRTYPSDFGHJKLÇZXCVBNM':
            traducao = traducao + palavra[x]
        else:
            traducao = traducao + palavra[x] + 'p' + palavra[x]
    return traducao