def primo(numero):
    """dado um número inteiro positivo,
verifica se este número é primo
ou não. Retorna um valor booleano"""

    a = numero%2 #exemplo, caso o numero for divisel por 2, será divisel por 1 e ele mesmo
    b = numero%3 #logo, ele não será primo
    c = numero%5
    d = numero%7 #utilizei apenas o principais numeros, pois, por exemplo, 4 é 2+2 então não é necessário coloca-lo
    
    if (a==0) or (b==0) or (c==0) or(d==0):
        return False


    else:
        return True