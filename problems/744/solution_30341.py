# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(texto):
    """Dado um texto qualquer,se a quantidade de caracteres for par,
    retona # no início, meio e fim; e se for ímpar, retorna # no início,
    meio deslocado para a parte par do texto e no fim:
    str--->str"""
    len_texto=len(texto)
    lim_texto=len_texto//2
    return '#'+texto[0:lim_texto]+'#'+texto[lim_texto:len_texto]+'#'