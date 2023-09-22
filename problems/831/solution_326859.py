def lingua_p(palavra):
    a=str.replace(palavra,'a','apa')
	b=str.replace(a,'e','epe')
	c=str.replace(b,'i','ipi')   
    d=str.replace(c,'o','opo')
    e=str.replace(d,'u','upu')
    A=str.replace(e,'á','ápá')
	B=str.replace(A,'é','épé')
	C=str.replace(B,'í','ípí')   
    D=str.replace(C,'ó','ópó')
    E=str.replace(D,'ú','úpú')
    return E