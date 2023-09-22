def carros (p,c=5):
    '''calcula  o numero exato de carros necessarios para a realizacao de uma viagem com base no numero de passageiros(p) e a capacidade (c) caso o veiculo nao seja convencional.'''
    if p % c != 0:  
        p += 1
        return round(p/c)