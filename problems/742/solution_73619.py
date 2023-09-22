# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    'Função que retorna o valor de s, sendo que i tem que ser substituido por x'
    return s[:i]+x+[i+1:]