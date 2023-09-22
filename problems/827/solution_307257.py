def qtd_divisores(número):
    "Função que conta quantos divisores um dado número inteiro dado de entrada tem. int --> int"
    divisores=0
    for i in range(1,número+1):
        if número%i==0:
            divisores=divisores+1
    return divisores