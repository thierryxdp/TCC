def lingua_p(palavra):
    """funcao que dada uma palavra, retorna sua traducao para a lingua P, que insere uma sequencia de letras 'p' mais a vogal apos reconhcer uma vogal na palvra.
    str--->str"""
    palvra=str.lower(palavra)
    for elem in range(len(palavra)):
        if palavra[elem]=='aeiou':
            palavra[elem]=palavra+'p'+palavra[elem]
    return palavra