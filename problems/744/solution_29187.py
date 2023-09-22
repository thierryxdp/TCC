# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Recebe uma string s e retorna uma string com um hashtag
    no início, no meio e no final dela, no caso do meio da string
    não coincidir com um indíce, o meio será considerado o menor
    índice mais próximo;
    string -> string"""
    indice_meio = len(s)//2
    return "#" + s[:indice_meio + 1] + "#"