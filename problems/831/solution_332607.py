def lingua_p(palavra):
    traduzido_p = ''
    for vogal in range(len(palavra)):
        if palavra[vogal] in 'aeiouéáú':
            traduzido_p = traduzido_p + palavra[vogal] + 'p'+palavra[vogal]
    return traduzido_p +palavra[vogal]