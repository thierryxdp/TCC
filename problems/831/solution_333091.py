def lingua_p(pal):
    '''Função que dada uma palavra, após cada vogal, incere a letra
p mais a vogal original e retorna esta nova palavra toda em minúscula.
str -> str'''
    minu = pal.lower()
    novapal = ''
    vogais = 'aeiouãáàéêíóôõúAEIOUÃÁÀÉÍÓÔÕÚ'
    for p in minu:
        novapal += p
        if p in vogais:
            novapal += 'p' + p
    return novapal