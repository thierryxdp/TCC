# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que retorna uma string onde x é substituido por i"""
    """string, string, int --> string"""
    a = s[0:(i)]
    b = s[(i+1):(len(s))]
    return (str(a) + str(x) + str(b))