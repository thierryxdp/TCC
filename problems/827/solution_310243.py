def qtd_divisores(numero):
    'função que recebe um número e retorna quanto divisores ele tem. int->int'
    divisores=()
    i=1
    for proximo in numero:
        if numero%i==0:
            divisores+=([i],)
        i+=1
    return divisores