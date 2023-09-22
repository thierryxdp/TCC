def lingua_p(palavra):
    """funcao que dada uma palavra, retorna sua traducao para a lingua P, que insere uma sequencia de letras 'p' mais a vogal apos reconhcer uma vogal na palvra.
    str--->str"""
    palavra=str.lower(palavra)
    palavra_nova=''
    for elem in range(len(palavra)):
        if palavra[elem] in 'aeiouáé':
            palavra_nova=palavra_nova+palavra[elem]+'p'+palavra[elem]
        else:
            palavra_nova=palavra_nova+palavra[elem]
    return palavra_nova