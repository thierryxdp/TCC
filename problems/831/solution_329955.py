def lingua_p(palavra):
    """
		Retorna a palavra na lingua do P.
        str -> str
    """
    vogais=['a','e','i','o','u']
    nova_palavra=''
    for l in palavra:
        if l in vogais:
            nova_palavra= nova_palavra+l+'p'+l
        else:
            nova_palavra=nova_palavra+l
    return nova_palavra