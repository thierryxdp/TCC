# Função que, dados a e b sendo strings, retorna uma única string no formato 'abba''
# str, str -> str
def concatenacao(a, b):
    return (a,b) + (b,a)