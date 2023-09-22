"Dada uma  frase, retorna a frase onde todos  os caracteres foram substituidos por espaço"
    "str --> str"
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace('.',' ')
    frase = frase.replace('...',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace(':',' ')
    frase = frase.replace(';',' ')
    frase = frase.replace('-',' ')
    return frase