def colchao(medidas,H,L):
        medidas = [int(b), int(c)]
        if H + L >= b + c:
            return "False"
        if H + L < b - c:
            return "True"