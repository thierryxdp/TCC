# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna uma nova string s com o caracter x trocado pelo caractere da posição i
    str, str, int -> str"""
    pos=i+1
    nova_str=s[:i]+x+s[pos:]
    return nova_str