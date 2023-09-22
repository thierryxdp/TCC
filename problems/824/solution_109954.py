def uppCons(frase):
    maiuscula=''.join(vogal.upper() if vogal in 'aeiou' else vogal for vogal in frase)
    return maiuscula