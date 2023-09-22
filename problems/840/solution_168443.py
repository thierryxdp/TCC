def bolos(a,b,c):
    'retorna a quantidade maxima de bolos dados A xicara de farinha de trigo,B ovos e C colheres de sopa de leite'
    if a<2:
	    return 0
    elif b<3:
	    return 0
    elif c<5:
	    return 0
    else:
	    return (a//2+b//3+c//5)//3