def carros(pessoas,capacidade=5):
    """calcula e retorna a quantidade de carros necessários dada uma certa quantidade de pessoas. int,int->int"""
    if(pessoas%capacidade!=0):
        return (pessoas// capacidade)+1
    else:
        return pessoas//capacidade