def lingua_p(palavra):
    '''funcao que a palavra de entrada convertida na linga do P,
    a qual é inserida a respectiva sequencia da letra P a cada vogal da 
    palavra em conjunto com a vogal original.
    string -> string'''
    palavra_p = palavra[:]
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            substituto = letra + 'p' + letra
            palavra_p = str.replace(palavra_p,letra,substituto)
    return palavra_p