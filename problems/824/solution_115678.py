def uppCons (frase):
    """dada uma frase, retorna a frase com todas as consoantes em maiusculo;
    str->str."""
    cons='bcdfghjklmnpqrstvwxyzç'
    p=0
    while p< len(cons):
        frase=frase.replace(cons[p],cons[p].upper())
        p=p+1
    return frase