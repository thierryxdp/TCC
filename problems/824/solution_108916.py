def uppCons (frase):
    """funçao que recebe uma frase e retorna a frase com suas consoantes em letras maiusculas
    entrada: str;
    saida: str."""
    pos = 0
    nova_str = ''
    consoante = 'bcdfghjklmnpqrstvxyzç'
    while pos < len(frase):
        if frase [pos] in consoante:
            nova_str += str.upper(frase [pos])
        else:
            nova_str += frase [pos]
        pos +=1
    return ''