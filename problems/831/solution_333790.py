def lingua_p(palavra):
    traduz_p = []
    contagem = 0
    limit = len(palavra)

    while contagem < limit:
        if palavra[contagem] in 'aeiouáéíóú':
            traduz_p.append(palavra[contagem] + 'p' + palavra[contagem])
        else:
            traduz_p.append(palavra[contagem])  

        contagem += 1