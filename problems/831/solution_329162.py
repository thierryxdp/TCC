def lingua_p(palavra):
    palavra_minuscula= palavra.lower()
    letras = list(palavra_minuscula)
    
    index = 0
    for vogal in letras:
        if vogal in "aeiouáéíóúâêîôû":
            linguap = 'p' + vogal
            list.insert(letras,index+1,linguap)
        index += 1
    palavra_traduzida = ''.join(letras)
    
        
        
    return palavra_traduzida