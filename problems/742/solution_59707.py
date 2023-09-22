# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''funcao que recebe uma string s, um caractere x e um numero i, e retorna a string passada
       com a alteracao do elemento na posicao i
       OBS: e preciso colocar uma posicao i que seja menor ou igual ao tamanho da string
       string, string, int -> string'''
    if (len(s) < i-1):
        return 'impossivel realizar a operacao de troca do elemento, pois a posicao selecionada nao se encontra dentro da string'
    else:
        parte1 = s[:i]
        parte2 = x + s[i+1:]
        return parte1 + parte2