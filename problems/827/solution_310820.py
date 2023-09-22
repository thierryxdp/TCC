def qtd_divisores(x):
    ''' Esta função ao inserir um valor, calcule a quantidade de divisores estiver
    assinatura int -> int'''
    resultado = [i for i in range(1, x+1) if x% i==0]
    return len(resultado)