# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    lista = list(s)
    metade = int(len(s)/2)
    lista_final = ["#"]
    lista_final += lista[:metade]
    lista_final += "#"
    lista_final += lista[metade:]
    lista_final += "#"
    return ''.join(lista_final)