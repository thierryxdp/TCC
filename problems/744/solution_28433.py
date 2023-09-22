# função que recebe umastring e retorna com o caractere "#" no inicio, meio e fim da string
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(texto):
    comeco = len(texto)//2
    final = -len(texto)//2
    return '#' + texto[:comeco]+'#'+texto[final:]+'#'