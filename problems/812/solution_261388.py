def remover(texto, remove):
    string = texto
    for x in remove:
        string = string.replace('.', ' ') +string.replace(':', ' ')+string.replace('-', ' ')+string.replace(';', ' ')+string.replace(',', '')
    return string