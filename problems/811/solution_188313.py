def colchao((medidas),H,L):
        medidas[1] = b
        medidas[2] = c
        if H + L >= b + c:
            return "False"
        if H + L < b - c:
            return "True"