def carros(num_pessoas, vagas = 5):
    """Função para calcular a quantidade de carros necessária para realizar uma viagem.
       Onde: "num_pessoas" é a quantidade de pessoas que participarão da viagem;
             "vagas" é a quantidade de pessoas que cabem no veículo (default = 5)."""
    import ceil from math
    return ceil(num_pessoas // vagas)