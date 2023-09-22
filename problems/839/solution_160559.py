import numpy as np
def carros (passageiros,capacidade=5):
    if capacidade ==5:
        n_carros = np.ceil(passageiros/5)
        else:
            n_carros = np.ceil(passageiros/capacidade)
return n_carros