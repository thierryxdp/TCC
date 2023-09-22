def carros(pessoas,capacidade==5):
    """Função que calcula e retorna o número de carros necessários para uma viagem
       dados o número de pessoas e a capacidade dos veículos.
       int,int->int
       
       Parâmetros:
       pessoas: Número de pessoas que irão viajar.
       capacidade: capacidade máxima que os veículos conseguem carregar de pessoas.
       
       returns: O número de veículos necessários para a viagem.
       """
    
    if ((pessoas%capacidade)>0):
        return pessoas//capacidade+1
    else:
        return pessoas/capacidade