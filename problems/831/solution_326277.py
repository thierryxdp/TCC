def lingua_p(palavra):
    """lççdfldsf"""
    
    p = []
    
    for i in palavra:
        if palavra[i] in 'BbCcDdFfGHhgJjKkLlMmNnPpQqRrSsTtVvWwXxZzç':
             palavra = palavra.replace(palavra[i],'p'+ palavra[i].lower())
    return palavra