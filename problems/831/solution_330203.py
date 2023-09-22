def lingua_p(palavra):
    minuscula=palavra.lower()
    tradução=[]
    for i in range (len(palavra)):
        if palavra[i] in 'aeiou':
            tradução.append(palavra[i])
            tradução.append('p')
            tradução.append(palavra[i])
        if palavra[i] in 'bcdfghjklmnpqrstvwxyzç':
            tradução.append(palavra[i])
    return ''.join(tradução)