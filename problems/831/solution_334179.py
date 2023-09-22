def lingua_p(palavra):
    """recebe uma palavra em portugues e retorna a palavra traduzida na "lingua do p""""
    vogais='aeiouáéíóàãõôâêú'
    str.lower(palavra)
    c = 0
    
    for i in palavra:
        if i in vogais:
            palavra = palavra[:c+1] + 'p' + i + palavra[c+1:]
            c = c+2
        c = c+1
        
    return palavra