def busca(setor, dados):
    return [funcionario for funcionario in dados if funcionario.pop(2) == setor]