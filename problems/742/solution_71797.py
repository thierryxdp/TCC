# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    new_s=s #Criar uma sub-variável para tornar S em mutável
    return new_s[0:i] + x + new_s[i + 1:] #Método da concatenação estipulando pausa e continuação da palavra.