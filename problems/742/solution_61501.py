# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que recebe uma string s , um caractere s e um int i,
    e retorna a str s exceto que o elemento da posiçao i será substituido
    pelo caractere x,str,str,int-->str """
    return s[:i] + x + s[i+1:]