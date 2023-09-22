def lingua_p(palavra):
    '''Função que recebe uma palavra em português e retorna a palavra
    na língua do P
    
    str->str'''
    
    vogal = "aáàâãeéèêêiíìîoóòôõuúùû"
    
    palavra = palavra.lower()
    
    palavra_p = ""
    
    for letra in palavra:
        palavra_p = palavra_p + letra
        if letra in vogal:
            palavra_p = palavra_p + "p" + letra
            
    return palavra_p