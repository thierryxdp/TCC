# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Dado uma palavra s, um caractere qualquer x, e um número inteiro i, a função irá substituir a letra na posição i da palavra s pelo caractere x. Sendo s, x uma string e i um inteiro."""
    palavra = s
    numero_recebido = i
    return palavra[0:numero_recebido] + x + palavra[numero_recebido+1:]