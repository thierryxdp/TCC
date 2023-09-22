def busca (chave,matriz):
    pessoa1 = matriz[0]
    pessoa2 = matriz[1]
    pessoa3 = matriz[2]
    if chave in pessoa1:
        list.remove(pessoa1,chave)
        dados = pessoa1
    if chave in pessoa2:
        list.remove(pessoa2,chave)
        dados = pessoa2
    if chave in pessoa3:
        list.remove(pessoa3,chave)
        dados = pessoa3
    else: 
        dados = []
    
	return [dados]