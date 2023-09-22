def lingua_p(palavra):
    """Funcao calcula e returna a letra 'p' depois de uma vogal;
    str->str"""
    nova=''
    for letra in palavra:
        if letra.lower() in 'aeiouáéíóú':
            nova=nova+letra+'p'+letra
        else:
            nova=nova+letra
    return nova.lower()