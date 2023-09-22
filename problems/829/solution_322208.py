def soma_h(numero):
    """A função calcula o valor de H da equação 
    (H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N). A equação 
    tem N termos, onde N deve ser dado como parâmetro.
    O valor de H é retornado com 2 casas decimais;
    int --> float"""
    lista_para_soma = []
    lista_para_numeros = list(range(1, (numero+1)))
    for num in lista_para_numeros:
        list.append(lista_para_soma, (1/num))
    soma = sum(lista_para_soma)
    return round(soma,2)