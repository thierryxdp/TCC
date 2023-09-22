# Retorna se é possível passar o colchão pela porta
	def colchao (medidas,H,L):
        """
        Retorna se é possível passar o colchão pela porta
        list, int, int -> bool
        """
        if medidas[1]<=H:
            return True
        else:
            return False