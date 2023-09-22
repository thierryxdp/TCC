import math
def carros(p, v=5):
	"calcula quantos carros sao necessarios para a viagem, sendo p pessoas e v vagas"
	return math.ceil(p/v)