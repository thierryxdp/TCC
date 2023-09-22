def posLetra(frase,letra,numero):
    i = 0
    letra = numero.index(i)
    while letra in len(frase):
        letra = letra.index(numero)
         i = i + 1
        return letra
    else:
          return - 1