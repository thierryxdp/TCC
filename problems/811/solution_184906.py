def colchao(lista,H,L):
        """"Função que retorna um bool se o colchao passa ou não
        int, int -> bool"""
        A = lista[0]
        B = lista[1]
        
        if (B<=H and A<=L) or (B<=L and A<=H):
            return True
        else:
            return False