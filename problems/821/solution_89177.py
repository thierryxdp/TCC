def fatorial(fat):
    """A função retorna o fatorial do numero dado;
	int->int"""
    i = 1
    while fat > 1:
        i *= fat
        fat = fat -1
    return i