def lingua_p(palavra):
    """ Função que recebe uma palavra e retorna esta mesma
    palavra na língua do P
    Entrada: str
    Saída: str """
    traduzido_p = ''
    for vogal in range(len(palavra)):
        if palavra[vogal] in 'aeiouéáú':
            traduzido_p = traduzido_p + palavra[vogal] + 'p' + palavra[vogal]
        else:
             traduzido_p = traduzido_p+palavra[vogal]
    return traduzido_p