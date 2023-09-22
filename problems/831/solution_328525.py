def lingua_p(palavra):
    """Função que recebe uma palavra e a transcreve para a lingua do P
    str -> str"""
    string =''
    for i in range (0,len(palavra)):
        if palavra[i] in ['a','e','i','o','u']:
            string = string + palavra[i] + 'p' + palavra[i]
        else:
            string = string + palavra[i]
        
    return string.lower()