def lingua_p(palavra):
    '''função que traduz uma palavra para a língua do p
    str->str'''
    
    v = "aáàâãeéèêêiíìîoóòôõuúùû"
    
    palavra = palavra.lower()
    nova_palavra = ""
    for letra in palavra:
        nova_palavra += letra
        if letra in v:
            nova_palavra += "p" + letra
            
    return nova_palavra