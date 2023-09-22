def lingua_p(palavra):
    p=str.lower(palavra)
    v=''
    vogais['a','e','i','o','u','á','é','í','ó','ú','â','ê','ô','û','ã','õ']
    for x in p:
        if x in vogais:
            v=v+x+'p'+x
        else:
            v=v+x
    return v