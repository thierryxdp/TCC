def soma_h(numero):
    """dado um numero, afunção calcula H e retorna um resultado com 2 casas decimais
    	
        int->float"""
    	H=1
        indice=2
        while indice <=numero:
            H=H+1/indice
            indice=indice+1
            return round(H,2)