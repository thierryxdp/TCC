# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Função que dada uma string retorna a mesma string, com um caractere diferente, dado a posição do caractere q vai ser alterado e o novo elemento.
    Assinatura string, int, int -> string
    Caso teste:
    'casa','t',2 == cata
    'pipoca','v',2 == pivoca
    frase = s
    len(frase)
    sub_01 = frase[0:(i)]
    return sub_01 + x + (frase[(i+1):(len(frase))])