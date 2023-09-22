def retira_pontuacao(f):
    """A função acima retorna a str f com todas as suas pontuações substituidas por espaço.
       str -> str"""
    f = str.replace(f, '-', ' ')
    f = str.replace(f, ',', ' ')
    f = str.replace(f, ':', ' ')
    f = str.replace(f, ';', ' ')
    f = str.replace(f, '.', ' ')
    f = str.replace(f, '!', ' ')
    f = str.replace(f, '?', ' ')
    f = str.replace(f, '...', '.')
    return f
#Teste 1:
#retira_pontuacao('