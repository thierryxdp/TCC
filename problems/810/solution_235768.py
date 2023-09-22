def inverte(x):
    x = x.replace('.', ' ')
    x = x.replace(',', ' ')
    x = x.replace(':', ' ')
    x = x.replace(';', ' ')
    x = x.replace('!', ' ')
    x = x.replace('?', ' ')
    x = x.replace('-', ' ')
    x = x.replace('"', ' ')
    x = x.lower()
    x = x.split()
    x = x[::-1]
    x = ' '.join(x)
    return x