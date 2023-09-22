def qtd_divisores(numero):
    'retorna total de numeros que dividem o numero dado'
    'int--int'
    i=1
    soma=0
    while i<= numero:
        if numero%i==0:
            soma+=1
        i= i+1
    return soma