def inverte(f:str):
     "recebe uma frase(f) e inverte ela tirando todas as pontuações e letras maiusculas"
    f = f.lower()
    f = f.replace(',', ' ')
    f = f.replace(';', ' ')
    f = f.replace(':', ' ')
    f = f.replace('...', ' ')
    f = f.replace('.', ' ')
    f = f.replace('!', ' ')
    f = f.replace('?', ' ')
    f = f.replace('-', ' ')
    lista = str.split(f)
    lista.reverse()
    f = str.join(" ", lista)
    return f