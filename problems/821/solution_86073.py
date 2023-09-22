def fatorial(x):
    "função que calcula o fatorial do número recebido" 
    ft = 1
    while x > 0:
         ft = ft*x
         x = x - 1
    if x < 0:
        ft = "indefinido"
    return ft