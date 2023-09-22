def carros (p,c=5):
    '''calcula  o numero exato de carros necessarios para a realizacao de uma viagem com base no numero de passageiros(p) e a capacidade (c) caso o veiculo nao seja convencional.'''
    if c < 5:
        return round(p/c)
    elif p > 5:
        return round(((p/c)+0.5))
    elif 0 < p <= 5:
        return 1
    elif p == 0:
        return 0