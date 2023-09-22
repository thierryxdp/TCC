def melhor_volta(corrida):
    """Primeiramente, atribui a três variáveis, o valor do menor tempo do primeiro corredor,
    seu número, e o número da volta correspondente ao valor, a partir desse valor a função
    fará comparação com os outros corredores. Para cada corredor dos restantes,
    é verificado se seu menor valor é menor que o do corredor mais rápido atual,
    caso sim, muda o tempo anterior para o deste corredor, atribui a variável do corredor
    mais veloz o número desse corredor, e encontra a volta correspondente ao tempo e a atribui
    a variável da volta. Caso o corredor não seja mais rápido a função verifica o próximo.
    Após todos serem verificados, retorna o número do corredor, o tempo e a volta correspondente.
	"""
    menor=min(corrida[0])
    veloz=1
    volta=corrida[0].index(menor)+1
    for corredor in range(1,6):
        if min(corrida[corredor])<menor:
            menor=min(corrida[corredor])
            veloz=corredor+1
            volta=corrida[corredor].index(menor)+1
    return (veloz,menor,volta)