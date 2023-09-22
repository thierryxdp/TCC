import math
def carros(pessoas,capacidade=5):

   '''calcula e retorna o numero exato de carros necessarios para uma viagem'''

   auto = math.ceil(pessoas / capacidade)

   return auto