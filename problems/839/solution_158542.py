def carros(n_pessoas,qt_veiculo=5):
    '''calcula e retorna a quantidade de carros necessários para a viagem
 	entrada: int,int -> int'''   
    qt_total = math.ceil(n_pessoas / qt_veiculo)
    return qt_total