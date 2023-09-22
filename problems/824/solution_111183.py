def uppCons (frase):
    """função que recebe uma frase e a retorna com as consoantes em maiusculo"""
    """string -> string"""
    letra = 1
    final = frase[0].upper()
    while letra < len(frase):
        if frase[letra] in ('b','B','c','C','ç','Ç','d','D','f','F','g','G','h','H',
                            'j','J','k','K','l','L','m','M','n','N',
                            'p','P','q','Q','r','R','s','S','t','T','v','V',
                            'w','W','x','X','y','Y','z','Z'):
            final += frase[letra].upper()
        else:
            final += frase[letra].lower()
        letra += 1

    return final