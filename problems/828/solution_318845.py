def primo(n):
 """Dado um int n, retorna se ele é primo ou não
    assinatura:
    int -> bool
    testes: 
    primo(3) == "True"
    primo(4) == "False" """
	if qtd_divisores(n)== 2:
    	return "True"
 	else:
    	return "False"