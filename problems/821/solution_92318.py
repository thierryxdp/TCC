def fatorial (n):
  """ Esta função calcula o fatorial de um número
assinatura int -› int """
     fat = 1
     for c in range(n , 0, -1):
        fat *= c
    return fat