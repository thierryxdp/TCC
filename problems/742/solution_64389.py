# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que retorna uma string s, retirando-se o elemento da posição i e substituindo por um caractere x
    entrada: string, string, int
    saida: string"""
    s[0:i] + str(x) + s[i+1:]