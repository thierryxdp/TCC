def bolos(farinha,ovos,leite):
    '''funcao que calcula a quantidade de bolos possíveis
em ser realizados de acordo com os ingredientes dados, como pedido na
receita que indica que devem ser usadas 2 xicaras de farinha de trigo,
3 ovos e 5 colheres de sopa de leite.(farinha, ovos, leite).'''

    return min ((farinha//2),(ovos//3),(leite//5))