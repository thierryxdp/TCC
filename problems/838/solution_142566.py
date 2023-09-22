import math
def num_bombons(din,pr):
    """Função que calcula quantos bombons podem ser comprados a partir
  do dinheiro disponível "din" e o preço de cada bombom "pr"
  float,float ->int """
    return math.floor(din/pr)