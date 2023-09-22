def lingua_p(palavra):
    palavra = palavra.lower()
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    palavra_traduzida = ''
    
    for letra in palavra:
        if letra in consoantes:
            palavra_traduzida += letra
        else:
            palavra_traduzida += letra + 'p' + letra
            
    return palavra_traduzida