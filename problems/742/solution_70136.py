# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """A função que dada uma string, um caracter e um índice 
    na string, respectivamente, substitui o caractere no índice
    i pelo novo caractere x"""
    nletras = len(s)
    if(i <= nletras):
        nome = s
        nome2 = nome[0:i]
        return nome2 + str(x)+ nome[i+1:]
    else:
        return 'Por favor, informe um índice válido para a string'