# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def meio(x):
    return (len(x))/2
"""retorna o sinal #, o corte da string começando na posição zero e terminando na metade da palavra (dada a função auxiliar para a definição da posição que marca o meio da palavra), encerrando com outro sinal #
    string -> string"""
def hashtag(s):
    return "#"+x[0:meio(s)]+"#"+x[meio(s):len(s)]+"#"