def lingua_p(palavra):
    """Função que converte a palavra de entrada na mesma
    palavra só que na linguagem do p"""
    palavra_p = ''
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    for letra in palavra:
        if str.lower(letra) not in consoantes:
            substituto = letra + 'p' + letra
            palavra_p += substituto
        if str.lower(letra) in consoantes:
            palavra_p