# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    
    """Substitui um valor dentro da string s pelo valor x 
    informado, de acordo com a posição i informada em 
    relação a s.
    string, int, int -> string"""
    
    return str.replace (s, str (s[i]), str (x), 1)