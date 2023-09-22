def lingua_p(palavra):
    contagem = 0
    limit = len(palavra)
    tradutor_p = []
    while contagem < limit:
        if palavra[contagem] in 'aoieiíúéá':
            tradutor_p.append(palavra[contagem] + 'p' + palavra[contagem])
        else:
            tradutor_p.append(palavra[contagem])
            contagem += 1
return ''.join(tradutor_p)