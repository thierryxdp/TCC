def carros(nPessoas,capacidade=5):
   '''calcula o número exato de carros necessários para uma viagem, 
   dados o número de pessoas e a capacidade de veículos, caso seja
   dada apenas um parâmetro a capacidade será = 5'''
return (math.ceil(nPessoas/capacidade))