# substitui Strings
# string, int, int -> string
def substitui(palavra, letra, posicao):
    return palavra[:posicao] + letra + palavra[posicao+1:]