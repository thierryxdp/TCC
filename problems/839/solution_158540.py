def carros(n_pessoas=5,qt_veiculo):
    '''calcula e retorna a quantidade de carros necessários para a viagem
 	entrada: int,int -> int'''   
    qt_total = n_pessoas / qt_veiculo
    return round(qt_total)