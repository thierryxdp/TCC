def carros(pessoas,vagas=5):
    """Essa função calcula a quantidade de carros necessarios para uma viagem.
    Recebe números de pessoas e quantidade de vagas.
    Retorna quantidade de carros necessarios."""
    return max(pessoas/vagas)
#int,int → int