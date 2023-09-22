def fatorial(numero):
    """A função abaixo calcula o fatorial de um determinado número utilizado o laço em while,
no qual um contador iniciado em 1 é executado até que este seja igual ao número de
componentes contidos em (range(numero))."""
    contador = 1
    resultado = 1
    while contador<=len(range(numero)):
          resultado = resultado * contador
          contador  = contador + 1
    return resultado