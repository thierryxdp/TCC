# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Coloca # no início, meio e fim da função"""
    y = len(s)/2
    return f"# {s[0:len(s)/2-1]} # {s[-1:-len(s)/2:-1]} #"