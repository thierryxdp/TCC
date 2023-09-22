def fatorial (numero):
    "função que dado um número, retorna o seu fatorial.int->int."
    produto = 1
    vezes = 1
    while vezes <= numero:
        produto = produto*(vezes)
        vezes = vezes+1
    return produto