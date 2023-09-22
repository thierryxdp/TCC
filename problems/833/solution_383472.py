def conta_numero(numero, matriz):
    """Recebe um número e uma matrizde números inteiros e retorna quantas vezes
       esse número aparece na matriz.
       int,list->int

       numero: Um número inteiro.
       matriz: Uma matriz matematica de números inteiros."""
    contador=0
    for linha in matriz:
        for n in linha:
            if n == numero:
                contador=contador+1
    return contador