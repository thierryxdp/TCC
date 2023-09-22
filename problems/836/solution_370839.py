def busca(setores, L):
    '''Função que recebe uma matriz com o nome de funcionários com suas 
    respectivas informações, e faz uma busca por setor. str,list->list '''
    
    
    matriz = [["Adalberto Ferreira", "566", "Contabilidade", "(21)84564-5248"],
              ["Juliana Vasconcelos", "465", "RH", "(21)3555-4552"],
              ["Flavia Amorim", "565", "Contabilidade", "(21)2134-4845"]]
    dados = []
    for nome, registro, setor, fone in matriz:
        if setor == setores:
             dados.append([nome, registro, fone])
    return dados