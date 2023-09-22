def busca(busca_por_setor):
    matriz = [["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"],
              ["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"],
              ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]]
    dados = []
    for nome, rg, setor, telefone in matriz:
        if setor == busca_por_setor:
             dados.append([nome, registro, fone])
    return dados