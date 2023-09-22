def lingua_p(palavra):
    
    """
    str--->str
    Usa-se o comando for de forma padrão para se fazer o processo até 
    que acabe a palavra. Caso a leitura feita no momento seja a de uma
    vogal,se adiciona a vogal junto da letra p e da mesma vogal na string
    vazia.Caso a leitura nao seja de vogal,apenas adiciona-se essa 
    letra à string vazia.
    """
    
    palavra2=''
    
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouáéúíó':
            palavra2+=palavra[i]+'p'+palavra[i]
            
        else:
            palavra2+=palavra[i]
            
    return palavra2