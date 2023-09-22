def busca(setor_busca,matriz):
    return [  [nome, registro, fone] for nome, registro, setor, fone in matriz  if setor == setor_busca]