def uppCons(frase):
    """Retorna a frase dada com as consoantes em letras maiúsculas;
       str->str
       Parâmetros:
       frase: frase qualquer
    """
    i=0
    maiusculas=''
    while i<len(frase):
        if frase[i] not in 'bcdfghjklmnpqrstvxwyzç':
            maiusculas=maiusculas+frase[i]
        if frase[i] in 'bcdfghjklmnpqrstvxwyzç':
            n=str.upper(frase[i])
            maiusculas=maiusculas+n
        i=i+1
    return maiusculas