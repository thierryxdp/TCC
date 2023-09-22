# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna o valor da string ao inserir o caractere x no índice i"""
    return str(s)[0:i]+x+str(s)[i+1:]