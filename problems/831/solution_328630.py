def lingua_p(palavra):
    """Função que recebe como parâmetro uma palavra em português e retorna esta mesma palavra traduzida para a língua do P,
    str --> str"""
    string = ''
    for i in range(0,len(palavra)):
        if palavra[i] in ['a','e','i','o','u','á','é','í','ó','ú']:
            string = string + palavra[i] + 'p' + palavra[i]
        else:
            string = string + palavra[i]
        
    return string.lower()