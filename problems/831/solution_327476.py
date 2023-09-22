def lingua_p(palavra):
    '''A função traduzirá a palavra para a lingua do P, em que toda vez que ocorre uma vogal,
    será inserido a letra (p)
    dados de entrada -> string
    dados de saída -> string'''
    
    palavram = str.lower(palavra)
    letras = list(palavram)
    i = 0  #indice da lista
    Q = len(letras)
    
    while i <= Q:
        if letras[i] in ['a','e','i','o','u']:
            list.insert(letras,i+1,'p')
            list.insert(letras,i+2,letras[i])
         	
            i += +3

        else:
            i += +1
               
    junta_letras = "".join(letras)
    return junta_letras