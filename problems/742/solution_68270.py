# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Funcao que recebe uma string 's', um numero inteiro 'i' que e entre 0
        e o comprimento da string. Retorne uma string igual a 's', onde a
        posicao i deve ser substituida pelo caractere x.
        Entrada: str, int ; Saida: str'''
    
    novastring = s[0:i] + str(x) + s[i+1:]
    
    return novastring