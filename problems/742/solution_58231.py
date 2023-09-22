# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função para substituir o caracter de uma string.
       Onde: "s" - é a string que deseja modificar;
             "x" - é o novo caracter;
             "i" - é a posição do caracter que sera trocado.
       string, int, int -> string"""
    antes = s[:i]
    depois = s[i+1:]
    return antes + x + depois