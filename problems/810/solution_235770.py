def inverte(x):
    """dada uma frase, retorna ela invertida com os caracteres de pontuação 
    substituídas por espaço e tudo em letra minúscula"""
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