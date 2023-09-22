import: math
    def carros(num_pessoas,capacidade=5):
        ''' define o numero de carros necessarios para levar x pessoas para uma viagem
            int int ---> int '''
        return math.ceil (num_pessoas/capacidade)