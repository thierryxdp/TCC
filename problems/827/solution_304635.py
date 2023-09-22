def qtd_divisores():
    """Funcao que calcula a soma dos numeros fatoriais de 1 a 10. Int-->Int"""
    lista = range(1,11)
    fatorial = 1
    soma = 0
    
    for contador in lista:
        fatorial = fatorial * contador
        soma = fatorial + soma
    return soma