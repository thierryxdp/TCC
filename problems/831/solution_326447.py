def lingua_p(palavra):
    '''Escreva uma palavra para ser traduzida na lingua p. A lingua p
    transforma a palavra em minusculo e adiciona um p depois de cada
    vogal precedido pela repeticao da vogal.
    str -> str'''
    palavra_min=palavra.lower()
    em_p=''
    for l in palavra_min:
        if l in 'aeiouáéíóúã':
            l=l+'p'+l
        em_p=em_p+l
    return em_p