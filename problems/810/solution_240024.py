def retirar_pontuacao(txt):
    a = ['!','?','.',',',':',';','-']
    txt = txt.replace(0,' ')
    txt = txt.replace(1,' ')
    txt = txt.replace(2,' ')
    txt = txt.replace(3,' ')
    txt = txt.replace(4,' ')
    txt = txt.replace(5,' ')
    txt = txt.replace(6,' ')
	return txt

def inverte(txt):
    txt = txt.lower()
  	txt = retirar_pontuacao(txt) 
    txt = txt.split(' ')
    txt = txt.reverse()
    txt = str.join(txt," ")
    return txt