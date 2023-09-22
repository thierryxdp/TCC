def carros(pessoas,capacidade=5):
    """Calcula e retorna o numerp de carros necessarios para fazer uma viagem dado um numero de pessoa."""
    if pessoas/capacidade==0:
        return pessoas/capacidade
    else:
        return (pessoas/capacidade)+1