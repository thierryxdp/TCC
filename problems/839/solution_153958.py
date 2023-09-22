def carros(total_de_pessoas, capacidade=5):
    """Retorna o número mínimo de carros necessário para uma viagem com um dado número de pessoas e uma dada capacidade."""
    return math.floor(total_de_pessoas/capacidade)