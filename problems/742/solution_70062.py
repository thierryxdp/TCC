# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ Função que retorna a string s, exceto que o 
    elemento da posição i é substituido pelo caractere x.
    Entrada: tuple
    Saída: str"""
    nova = s[0:i] + x + s[i+1:]
    return nova