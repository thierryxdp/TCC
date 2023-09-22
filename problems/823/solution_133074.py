def faltante(l):
    " essa funcao recebe uma lista e retorna um numero inteiro, que nao pertence a lista de entrada; list-> int"
    l.sort()
    i=1
    while i in l:
        i=i+1
    return i