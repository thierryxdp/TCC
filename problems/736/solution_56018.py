# Função que retorna dois strings a e b concatenados, 
# no formato abba;
# str, str -> str
def concatenacao(a, b):
    X=(a,b)
    return X[0]+X[1]+X[1]+X[0]