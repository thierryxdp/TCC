# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funçao que recebe a string s substitui e o caractere da posição de numero i por x;
    entrada: str, str, int;
    saida: str."""
    
    troca = s [0: i]
    fim = s [i + 1:]
    return troca  + x + fim