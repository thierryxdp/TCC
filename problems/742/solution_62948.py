# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "Pega a string antes do i"
    primeira_parte = s[:i]
    "Pega a string depois do i, excluindo o caracter na posição i"
    ultima_parte = s[i+1:]
    " Junta a primeira parte + o caractere x + a ultima parte"
    uniao = primeira_parte + x + ultima_parte
    return uniao