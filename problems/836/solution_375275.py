def busca(setor, matriz):
  '''Função que, dado um setor e uma matriz, retorna os dados de todos os funcionários daquele setor
  str, matrix -> list'''

  dados = []

  for funcionario in matriz:
    '''Para cada funcionário na matriz (linha)'''
    for informacao in funcionario:
      '''Para cada informação desse funcionário (elemento)'''
      if informacao == setor:
        '''Se o setor pesquisado estiver entre as informações do funcionário, adicione os dados desse funcionário na lista final, excluindo o setor'''
        nome = funcionario[0]
        registro = funcionario[1]
        telefone = funcionario[3]
        dados += [[nome, registro, telefone]]

  return dados