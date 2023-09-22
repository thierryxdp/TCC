def busca(setor):
    matriz = [["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"],
              ["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"],
              ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]]
    nome = matriz[0][0], matriz[1][0], matriz[2][0]
    registro = matriz[0][1], matriz[1][1], matriz[2][1]
    setor = matriz[0][2], matriz[1][2], matriz[2][2]
    telefone = matriz[0][3], matriz[1][3], matriz[2][3]
    if setor == matriz[1][3]:
        return [nome[1][0], registro[1][1], telefone[1][3]]
    else:
        return [[nome[0][0], registro[0][1], telefone[0][3]], [nome[2][0], registro[2][1],