def carros(quantidade_de_pessoas):
    """Calcula e retorna o numero de carros necessarios para uma viagem entre amigos, dados a quantidade de pessoas que irão viajar"""
    return round((quantidade_de_pessoas/5)+ 0.5)

def carros_nao_convencionais(quantidade_de_pessoas, quantidade_de_pessoas_por_carro):
    return round((quantidade_de_pessoas/quantidade_de_pessoas_por_carro)+0.5)