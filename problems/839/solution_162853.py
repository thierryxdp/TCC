def carros(pessoas,capacidade=5):
"""funcao que retorna o numero de carros necessarios dependendo da quantidade de passageiros"""
if pessoas == 0:
        return 0:
        elif pessoas < capacidade or pessoas == capacidade and pessoas !=0:
            return 1:
            else pessoas % capacidade !=0:
                return (pessoas//capacidade)+1