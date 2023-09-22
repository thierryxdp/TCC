def carros(pessoas):
    '''Calcula o número exato de carros necessários para a viagem a partir do
    número de pessoas que viajarão
    
	Parâmetro:
   		pessoas - Número de pessoas que vão viajar
    
    Entrada: Int
    Saída: Int
    '''
    passageiros = pessoas//5
    if pessoas%5 != 0:
        passageiros = (pessoas//5)+1
    return passageiros