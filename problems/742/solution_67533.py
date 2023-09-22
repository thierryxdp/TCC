# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Recebe uma string s, um caractere x e um numero tipo inteiro entre 0 e o tamanho da string e retorna a string s com uma substituição  no índice i  pelo caractere x; str, str, int-> str .""" 
    sx=s[0:i]+str(x)+s[i+1:-2]
    return sx