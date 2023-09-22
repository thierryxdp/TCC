def colchao(medidas,H,L):
  '''Função que dados os parâmetros de entrada são uma lista com as dimensões do colchão em centímetros, ordenadas da menor para maior, e dois inteiros H e L, correspondentes respectivamente a altura e a largura das portas em centímetros, retornará True se o colchão passa pelas portas e False caso contrário'''
Ic=medidas[0]
ac=medidas[2]
cc=medidas[1]
if cc <=H or cc<=L:
    return True
elif ac<=H or ac<=L:
    return True
elif Ic<=L and Ic<=H:
    return False