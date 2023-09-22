def busca(setor,matriz):
    """Função que, dado o nome de um setor e uma matriz com informações dos funcionários de uma empresa, retorna as informações de todos os funcionários daquele setor; string,lista->lista"""
    
    funcionarios = []
    
    for lista in matriz:
        
        if lista[2] == setor:
            
            del lista[2]
            
            funcionarios = funcionarios + [lista]
            
    return funcionarios