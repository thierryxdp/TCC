# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dados a string (s), um caractere(x) e um 
    número inteiro (i) entre 0 e o comprimento da 
    string, retorna uma string igual exceto o elemento
    da posição (i) que foi subistituido pelo caractere(x)."""
    return s[0:i]+x+s[i+1:]