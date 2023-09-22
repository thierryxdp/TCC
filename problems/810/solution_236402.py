def inverte(txt):
	txt=txt.replace('?',' ')
	txt=txt.replace('.',' ')
	txt=txt.replace(';',' ')
	txt=txt.replace(':',' ')
	txt=txt.replace('!',' ')
	txt=txt.replace('-',' ')
	txt=txt.replace(',',' ')
	txt=txt.lower().split()
	txt=txt[-1::-1]
	txt=str.join(' ',txt)
	return txt