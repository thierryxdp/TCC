# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funcao que retorna a string s, mas com o seu termo indice i substituido por um caractere x;
    0<=i>=len(s);
    string, string, int -> string;
    string, float, int -> string"""
    return s[:i:1]+str(x)+s[i+1::]