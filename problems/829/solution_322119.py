def soma_h(n):
    """ calcula o valor da somatória até o n-ésimo termo dado
    retorno é arredondado para 2 casas decimais
    para valores maiores que zero
    entrada-> int
    retorn->float"""
    
    soma=0
    
    for i in range(n):
        soma=soma+(1/n)
        
    return round(soma,2)