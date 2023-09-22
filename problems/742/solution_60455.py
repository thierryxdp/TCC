# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s: str,x: str,i: int) -> str:
    '''Retorna a string s, exceto que na posição i troca-se o caracter antigo
    por x.'''
    return s[0:i] + x + s[i+1:len(s)]