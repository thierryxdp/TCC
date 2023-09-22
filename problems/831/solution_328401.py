def lingua_p(frase):
    """
    Função que recebe como paramêtro uma palavra e 
    a traduz para a lingua do p.
    string -> string
    
    """
    traducao = ''
    frase    = str.lower(frase)
    for i in frase:
        if i in 'aáàãâeéẽêiíìoòóôõuúù':
            traducao = traducao + i + 'p'+ i   
        else:
            traducao = traducao + i
    return traducao