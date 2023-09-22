def carros(p,c=5):
    """
    	Calcula o numero exato de carros necessarios para uma
        viajem com uma quantidade p de pessoas
        
        Parametros: 
        		p,c: int
        		Quantidade de pessoas e capacidade do carro
        Returns:
        		int
                Um numero representando a quantidade exata de carros
        """
    return round(p/c+0.4)