def inverte(txt):
    txt=txt.replace('?',' ')
	txt=txt.replace('.',' ')
	txt=txt.replace(';',' ')
	txt=txt.replace(':',' ')
	txt=txt.replace('!',' ')
	txt=txt.replace('-',' ')
	txt=txt.replace(',',' ')
	txt=txt.lower().split()
    txt=txt.reverse().join('0',txt)
    return txt