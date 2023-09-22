def remover(texto, remove):
    string = texto
    for '.' in remove:
        string = string.replace('.', ' ') +string.replace(':', ' ')+string.replace('-', ' ')+string.replace(';', ' ')+string.replace(',', '')
    return string