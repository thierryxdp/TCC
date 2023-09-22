def primo(numero):
    'Função que recebe um número e indica se ele é primo ou não.'
    'int->bool'
    lista=[]
    for divisor in range(1,numero+1):
        if numero%divisor==0:
            lista=lista+[divisor]
    if len(lista)==2:
        return True
    else:
        return False