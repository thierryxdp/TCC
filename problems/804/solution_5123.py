def filtra_pares(num1,num2,num3,num4):
    tupla_saida = ()
    if num1%2 == 0:
       tupla_saida= tupla_saida('num1')+tupla_saida
    if num2%2 == 0:
       tupla_saida= tupla_saida('num2')+tupla_saida
    if num3%2 == 0:
       tupla_saida= tupla_saida('num3')+tupla_saida
    if num4%2 == 0:
       tupla_saida= tupla_saida('num4')+tupla_saida
    return tupla_saida