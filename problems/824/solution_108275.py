def uppCons(frase):
    """Função que recebe uma frase e retorna a mesma frase, com a consoantes em maiusculas
    str --> str"""
    a=0
    consoante= ' '
    while a <len(frase):
        if frase[a] in 'bcdfghjklmnpqrstwxyzç':
            consoante = consoante + frase[a].upper()
        else:
            consoante= consoante + frase[a]
        a= a+1
        return consoante