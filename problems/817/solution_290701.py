def acima_da_media(x):
    """Função que calcula a quantidade de notas acima da média da turma;
    list -> list"""
    a = sum(x)
    b = len (x)
    media = a/b
    x += [media]
    list.sort (x)
    c = list.index(x,media)
    x = x[c+1:]
    if media in x:
    	list.remove(x,media)
    return x