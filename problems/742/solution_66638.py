# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Retorna a string s, porém com o valor da posição i
    substituído por 'x'
    str, str, int -> str"""
    return str(s[:int(i)]+str(x)+s[int(i)+1:])