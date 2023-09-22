def carros(a,b=4):
    """Retorna o numero de carros necessários para realizar uma viagem, 
    dado número de pessoas e quantidade de vagas no veículo caso não informe, 
    a função assume que o carro tem 4 vagas excluindo o assento do motorista."""
    return int(a/b)