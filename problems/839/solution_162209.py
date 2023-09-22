def carros (pessoas,veiculo=5):
    """Função que determina quantidade de carros para a viagem. Input int,int. Return int"""
    
    if pessoas%veiculo > 0:
        return (pessoas//veiculo)+1
    else:
        return pessoas//veiculo