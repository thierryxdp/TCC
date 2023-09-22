# Dadas duas strings a e b, queremos a concatenação
# de ambas no formato abba
# str, str -> str

def concatenacao(a, b):
    '''Dadas duas strings a e b, respectivamente, devolve a concatenação
    de ambas no formato abba;
    str, str -> str'''
    return (a + b + b + a)