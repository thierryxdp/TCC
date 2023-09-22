def busca(busca_por_setor):
    """Função que realiza uma busca pela matriz dada como entrada e retorna os dados de todos os funcionários de um determinado setor
list -> list"""

    matriz = [["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"],["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"],["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]]
    dados = []

    for nome, registro, setor, telefone in matriz:
        if setor == busca_por_setor:
            dados.append([nome,registro,telefone])
    return dados