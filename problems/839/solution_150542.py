import math
def carros(n_pessoas, cap_veiculos=5):
    return math.ceil(n_pessoas/cap_veiculos)
    #return n_pessoas//cap_veiculos + min(1,n_pessoas%cap_veiculos)