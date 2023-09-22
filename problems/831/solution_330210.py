def lingua_p(palavra):
    palavrinha = str.lower(palavra)
    for i in ('a','e','i','o','u'):
        p = i + 'p' + i
        lingua = str.replace(palavrinha,i,p)
    
    return lingua