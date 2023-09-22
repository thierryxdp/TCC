def lingua_p(palavra):
    '''A função traduzirá a palavra para a lingua do P, em que toda vez que ocorre uma vogal,
    será inserido a letra (p)
    dados de entrada -> string
    dados de saída -> string'''
    
    palavram = str.lower(palavra)
    letras = list(palavram)
    
    for i in letras:
        if i == ['a','e','i','o','u']:
            pos = list.index(letras,i)
            list.insert(letras,pos,'p')
            
    return letras