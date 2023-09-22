def hashtag(s):
    """Recebe uma string com # no inicio,meio e fim"""
    tamanho=len(s)
    metade=tamanho//2
    primeira_parte= s[:metade]
    segunda_parte=s[metade:]
    return "#"+primeira_parte+"#"+segunda_parte+"#"