def lingua_p(palavra):
    palavrinha = str.lower(palavra)
    for elem in ('a','e','i','o','u'):
        p = elem + 'p' + elem
        lingua = str.replace(palavrinha,elem,p)
    
    return lingua