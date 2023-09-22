def colchao(medidas,H,L):
  '''Função que dados os parâmetros de entrada são uma lista com as dimensões do colchão em centímetros, ordenadas da menor para maior, e dois inteiros H e L, correspondentes respectivamente a altura e a largura das portas em centímetros, retornará True se o colchão passa pelas portas e False caso contrário'''
lc=medidas[0]
ac=medidas[2]
cc=medidas[1]
if cc <=H or cc<=L:
    True
elif ac<=H or ac<=L:
    True
elif lc<=L and lc<=H:
    False