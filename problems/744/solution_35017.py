# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que dada uma string, retorna uma nova string porém com "#" no inicio meio e final.
    casos teste:
    ('abcd') == ('#ab#cd#')
    ('abcde') == ('#ab#cde#')
    ('sim') == ('#s#im#')
    assinatura str -> str"""
    frase = s
    k = len(frase)
    w = (int(k))/2
    if k % 2 == 0:
        return '#' + (frase[0:int(w)])+'#'+(frase[int(w):])+'#'
    elif k % 2 == 0:
        j = int(0.5-w)
        return'#' + (frase[0:int(j)])+'#'+(frase[int(j):])+'#'