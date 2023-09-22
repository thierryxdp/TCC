def  soma_h(numero):
    """Função que dado um numero, a função calcula e retorna o valor de H com N termos, a função deve me retornar um inteiro somente com duas 
duas casas decimais.  int->float"""
    
    H=1
    i=2
    
    while i <= numero:
        H=H+1/i
        i=i+1
    return round(H,2)