def hashtag(s):
    """A função retorna uma string a partir da string dada de parametro, só que com "#" no inicio
    no meio e no final da string.string-->string."""
    r=int(len(s)/2)
    return "#"+s[0:r]+"#"+s[r:]+"#"