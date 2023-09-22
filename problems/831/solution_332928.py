def lingua_p(frase):
    '''
    Funçao que dada uma frase, troque todas as vogais das palavras
    consideradas por pela mesma vogal e o p.
    '''
    frase_nova = frase[:]
    for vogal in ["a", "á", "à", "â", "ã", "e","é", "ê", "o",  "ó", "õ", "ô","u", "ú"]:
        frase_nova = str.replace(frase_nova, vogal,vogal+'p'+vogal)
    return frase_nova