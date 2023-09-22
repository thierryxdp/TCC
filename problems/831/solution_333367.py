def lingua_p(palavra):
    tr_p = []
    cont = 0
    for letras in list(palavra):
        if letras in 'aeiouáéíóúêô :
           tr_p.append(letras + 'p' + letras)
        else:
            tr_p.append(letras)
    return '' .join(tr_p)