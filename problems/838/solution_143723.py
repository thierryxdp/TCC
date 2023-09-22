def descontoIR(x):
    '''calcula  o valor dos descontos do IR de acordo com o salario bruto(x)'''
    if x<=2500:
        return x*0.11
    else:
        if x<=5000:
            return x*0.15
        else:
            return x*0.22
#Escreva sua função aqui. Pode apagar essa linha.