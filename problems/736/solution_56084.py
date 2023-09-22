# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str, str -> str
def concatenacao(a, b):
    lista = [a,b,b,a]
    lista.replace(' ','')
    final= ' '.join(lista)
    return final