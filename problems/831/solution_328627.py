def lingua_p(palavra):
    """..."""
    string = ''
    for i in range(0,len(palavra)):
        if palavra[i] in ['a','e','i','o','u','á','é','í','ó','ú']:
            string = string + palavra[i] + 'p' + palavra[i]
        else
            string = string + palavra[i]
        
    return string.lower()