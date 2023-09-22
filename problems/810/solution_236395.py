def inverte(txt):
    txt=txt.replace('?',' ').replace('.',' ').replace(';',' ').replace(':',' ')txt.replace('!',' ').replace('-',' ')0.replace(',',' ')
	txt=txt.lower().split()
    txt=txt.reverse().join('0',txt)
    return txt