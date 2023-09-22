def bolos(farinha,ovos,leite):
    "calcula a quantidade de bolos que se pode fazer dados os ingrediantes"
    return min(farinha//2,ovos//3,leite//5)