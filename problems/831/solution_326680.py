def lingua_p(palavra):
    'passa a palavra desejada para lingua do p, string --> string'
    palavra = palavra.lower()
    lista = []
    P = ''
    for i in (palavra):
        if i in ['a','e','i','o','u','é','ã','ô','õ','ê','à','â','á','ú']:
            P+= i + 'p' + i
        else:
            P+= i
    return P