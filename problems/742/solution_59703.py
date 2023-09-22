# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    caractere = str(x)
    numero = int(i)
    palavra = str(s)
    return palavra.replace((palavra[numero]),caractere)