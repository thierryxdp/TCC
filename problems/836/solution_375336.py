def busca(setor_busca,matriz):
    """função que recebe uma matriz e faz uma busca por setor, e retorna os dados de todos os funcionários daquele setor.
lista -> lista"""
    return [  [nome, registro, fone] 
            for nome, registro, setor, fone in matriz  
            if setor == setor_busca]