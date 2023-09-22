def colchao(medidas,H,L):
        medidas = int([a, b, c])
        if H + L >= b + c:
            return "False"
        if H + L < b - c:
            return "True"