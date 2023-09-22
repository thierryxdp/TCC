def qtd_divisores(n:int)-> int:
    ''''Conta quantos divisores o número recebido tem''''
    lista = list(range(1,n+1))
    def teste_divisor(num_lista):
        return True if n%num_lista==0 else False
    return len(list(filter(teste_divisor,lista)))