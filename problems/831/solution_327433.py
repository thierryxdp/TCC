def lingua_p(palavra):
    '''A função traduzirá a palavra para a lingua do P, em que toda vez que ocorre uma vogal,
    será inserido a letra (p)
    dados de entrada -> string
    dados de saída -> string'''
    
    Q = len(palavra)
    i= 0
    vogais = ['a','e','i','o','u']
    palavram = str.lower(palavra) #transformando a palavra toda em minuscula
    letras = list(palavram) #separando as letras da palavra
    
    while i <= Q:
        if i in vogais:
            list.insert(letras,i,'p')
            
    linguap = ''.join(letras)   
    return linguap