# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''dada uma str 's', retorna outra str semelhante, porem,
    com o elemento 'x' da posicao indicada 'i' substituido por
    caracter informado
    entrada: str, str, int
    saida: str'''
    rotulo = s
    meio_rotulo1 = rotulo[0:i]
    meio_rotulo2 = rotulo[i+1:]
    rotulo = meio_rotulo1 + x + meio_rotulo2
    return rotulo