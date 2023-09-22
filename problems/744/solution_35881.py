# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Coloca # no início, meio e fim da string"""
    if len (s) == 1:
    	return f"# {s[0]} #"
    elif len (s) == 2:
    	return f"# {s[0]} # {s[1]} #"
    elif len (s) == 3:
    	return f"# {s[0]} # {s[1]} {s[2]} #"
    elif len (s) >= 4:
        y = len(s)/2
    	return f"# {s[0:y-1} # {s[-1:-y:-1} #"