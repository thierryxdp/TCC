def uppCons(frase):
    """Retorna uma frase com todas as consoantes em maiusculas.str-->str"""
    i=0
    nova_frase=""
    while i<=len(frase):
        if frase[i] not in "AEIOUaeiou":
            nova_frase=nova_frase+str.upper(frase[i])
            i=i+1
        else:
            nova_frase=nova_frase+frase[i]
        	i=i+1
        return nova_frase