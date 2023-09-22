def intercala(texto):
    novo_texto = texto.replace('.', ' ')
    novo_texto = texto.replace('!', ' ')
    novo_texto = texto.replace('?', ' ')
    novo_texto = texto.replace('-', ' ')
    novo_texto = texto.replace(',', ' ')
    novo_texto = texto.replace(':', ' ')
    novo_texto = texto.replace(';', ' ')
    return novo_texto