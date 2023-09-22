def carros(numero_de_pessoas,quantidade_de_pessoas=5):
    '''calcula e retorna o número exato de carros necessários para a viagem
    int -> int'''
    return round((numero_de_pessoas/5)+0.4)