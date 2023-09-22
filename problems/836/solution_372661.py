def busca(s, m):
    """A função retorna os dados de todos os funcionários do setor s dado como parâmetro.
       str, lista -> lista
       Explicação: Dadas uma matriz m, referente aos dados dos funcionários de uma empresa, e um setor s,
                   a função busca em m todos os funcionários que são desse setor.
                   O setor pertencente é a terceira informação da lista de cada funcionário."""
    l = []
    for i in range(len(m)):
        if m[i][2] == s:
            list.append(l, [m[i][0], m[i][1], m[i][3]])
    return l
#Teste:
#m = [["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"], ["Juliana Vasconselos", "465", "RH", "(21)3555-4552"], ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]]
#busca("Contabilidade", m)--> [['Adalberto Ferreira', '566', '(21)84564-5248'],['Flavia Amorim', '565', '(22)2134-4845']]
#busca("Limpeza", m)--> []