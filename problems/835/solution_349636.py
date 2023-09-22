def melhor_volta(Matriz):
    ContadorColuna = 0
    ContadorLinha = 0
    Menor = min(Matriz[0])
        for Linha in Matriz:
            ContadorLinha +=1
            for Coluna in Linhas:
                ContadorColuna += 1
                if Menor == Coluna:
                    break
	return (ContadorLinha, Menor, ContadorColuna)