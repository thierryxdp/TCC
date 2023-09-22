def soma_h(n):
        #retornar o valor H com N termos onde N é inteiro e dado com entrada
        #entrada: n ; saida: res, com duas casas decimais
        res = 0
        for i in range(1, n + 1):
         h = 1 / i
         res += h
        return round(res, 2)