# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    
    meio = len(frase)//2
    tupla = str.partition(frase,frase[meio])
    return "#" + tupla[0] + "#" + tupla[1] + tupla[2] + "#"