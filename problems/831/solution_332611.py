def lingua_p(palavra):
    traduzido_p = ''
    for vogal in range(len(palavra)):
        if palavra[vogal] in 'aeiouéáú':
            traduzido_p = traduzido_p + palavra[vogal] + 'p'+palavra[vogal]
        else:
             traduzido_p = palavra[vogal] + traduzido_p
    return traduzido_p