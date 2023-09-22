# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "Pega a string antes do i"
    primeiraParte = [:i]
    "Pega a string depois do i, excluindo o caracter na posição i"
    ultimaParte = [i+1:]
    " Junta a primeira parte + o caractere x + a ultima parte"
    uniao = primeiraParte + x + ultimaParte
    return uniao