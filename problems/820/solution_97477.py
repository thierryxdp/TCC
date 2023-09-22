def posLetra(frase,letra,numero):
   	 ocorrencia = str.count(frase,letra)
        if ocorrencia < numero:
            return ('-1')
		else:
        return str.find(frase,letra,numero)