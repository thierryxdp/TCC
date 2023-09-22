def total(compras = [], dict = {}):
    contagem = 0
    for i in compras:
        contagem += dict[i]
   return round(contagem, 2)