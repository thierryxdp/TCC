def lingua_p(x):
    x = x.lower()
    palavrafinal = ''
    for y in x:
        if y in ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']:
            palavrafinal = palavrafinal + y + 'p' + y
        else:
            palavrafinal = palavrafinal + y
    return palavrafinal