def lingua_p(palavra):
    contador = 0
    limite = len(palavra)
    traduzido_p = []
    while contador < limite:
        if palavra[contador] in 'aoieiíúéá':
            traduzido_p.append(palavra[contador] + 'p' + palavra[contador])
        else:
            traduzido_p.append(palavra[contador])
            contador += 1
    return ''.join(traduzido_p)