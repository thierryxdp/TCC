def lingua_p(palavra):
    '''A função traduzirá a palavra para a lingua do P, em que toda vez que ocorre uma vogal,
    será inserido a letra (p)
    dados de entrada -> string
    dados de saída -> string'''
    
    vogais = ['a','e','i','o','u']
    palavram = str.lower(palavra) #transformando a palavra toda em minuscula
    letras = list(palavram) #separando as letras da palavra
    
    for i in letras:
        if i in vogais:
            pos = list.index(letras,i)
            list.insert(letras,pos,'p')
            
    linguap = ''.join(letras)   
    return linguap