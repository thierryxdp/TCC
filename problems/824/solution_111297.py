def uppCons (frase):
    """Função que retorna uma frase com todas as consoantes maiúsculas a partir de uma frase recebida
    str -> str"""
    x = 0
    frase2 = ''
    while x < len(frase):
        if (frase[x]) not in 'aàáãâeèéêiìíîoòõôuùúû':
            frase2 = frase2 + frase[x].upper()
        else:
            frase2= frase2 + frase[x].lower()
        x = x + 1
        return frase2