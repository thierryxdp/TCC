def lingua_p(palavra):
    '''funcao que a palavra de entrada convertida na linga do P,
    a qual é inserida a respectiva sequencia da letra P a cada vogal da 
    palavra em conjunto com a vogal original.
    string -> string'''
    palavra_p = ''
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    for letra in palavra:
        if str.lower(letra) not in consoantes:
            substituto = letra + 'p' + letra
            palavra_p += substituto
        if str.lower(letra) in consoantes:
            palavra_p += letra
    return palavra_p