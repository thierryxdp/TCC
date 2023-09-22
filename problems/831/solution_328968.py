def lingua_p(palavra):
    """funcao que dada uma palavra, retorna sua traducao para a lingua P, que insere uma sequencia de letras 'p' mais a vogal apos reconhcer uma vogal na palvra.
    str--->str"""
    palavra=str.lower(palavra)
    for elem in range(len(palavra)):
        if palavra[elem] in 'aeiou':
            n=1
            palavra=str.replace(palavra,palavra[elem],(palavra[elem]+'p'+palavra[elem]),n)
            n=n+1
    return palavra