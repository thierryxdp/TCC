def lingua_p(palavra):
    """Função que dada uma palavra em português, retorna ela traduzida na
    língua do P;
    string -> string"""
    palavra = palavra.lower()
    n_palavra=''
    for i in palavra:
        if i in ['a','á','ã','e','é','i','í','o','ó','u','ú']:
            n_palavra+= i+'p'+i
        else:
            n_palavra+= i
    return n_palavra