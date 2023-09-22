def carros(pessoas,capacidade=5):
    '''Calcula o número exato de carros necessários para a viagem a partir do
    número de pessoas que viajarão e da capacidade do veículo que será utilizado.
    Vale ressaltar que caso a capacidade do veículo não seja informada, ela será
    considerada 5, que é a capacidade de um veículo convencional
    
	Parâmetro:
   		pessoas - Número de pessoas que vão viajar
    	capacidade - Capacidade do veículo a ser utilizado
    Entrada: Int, Int
    Saída: Int
    '''
    passageiros = pessoas//capacidade
    if pessoas%capacidade != 0:
        passageiros = (pessoas//capacidade)+1
    return passageiros