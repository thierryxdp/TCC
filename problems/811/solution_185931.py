# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas,H,L):
  """
  funcao que recebe os valores das dimensoes de um colchao e as dimensoas do buraco da porta
  e verifica se ocorre alguma situacao onde eh possivel passar o colchao pela porta,
  dado no enunciado as restrições de como se fazer isso
  list, float, float ----- > boolean
  """
  x = medidas[0]
  y = medidas[1]
  z = medidas[2]
  
  return ((x<H and y<L)or(y<H and x<L)) or ((x<H and z<L)or(x<L and z< H)) or ((y<L and z<H)or(y<H and z<L))