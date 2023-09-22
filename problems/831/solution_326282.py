def lingua_p(palavra):
    """lççdfldsf"""
    
    p = []
    i = 0
    while i < len(palavra):
        if palavra[i] in 'BbCcDdFfGHhgJjKkLlMmNnPpQqRrSsTtVvWwXxZzç':
             palavra = palavra.replace(palavra[i],'p'+ palavra[i].lower())
    return palavra