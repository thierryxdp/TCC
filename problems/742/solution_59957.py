# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que substitui e retorna a uma string"""
    if 0 <= i <= len(s)-1:
        return s[:i]+str(x)+s[i+1:]