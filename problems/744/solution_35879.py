# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Coloca # no início, meio e fim da string"""
    if len (s) == 1:
    	return f "4 {s[0]} 4"
    elif len (s) == 2:
    	return f "4 {s[0]} 4 {s[1]} 4"
    elif len (s) == 3:
    	return f "4 {s[0]} 4 {s[1]}  {s[2]} 4"
    elif len (s) >= 4:
        y = len(s)/2
    	return f "4 {s[0:y-1} 4 {s[-1:-y:-1} 4"