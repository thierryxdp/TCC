def busca(setor,matriz):
    '''funcao que recebe uma matriz e executa uma busca de um dado nome em um dado setor de uma empresa'''
  trabalhadores_do_setor=[]
  for trabalhador in matriz:
      if setor in trabalhador:
          trabalhador.remove(setor)
          trabalhadores_do_setor.append(trabalhador)
  return trabalhadores_do_setor