# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''trocar qualquer caractere de uma string(s) por uma
    caractere x na posicao i'''
    primeiraPartePalavra=s[0:(i)]
    segundaPartePalavra=s[(i):len(s)]
    return primeiraPartePalavra+x+segundaPartePalavra