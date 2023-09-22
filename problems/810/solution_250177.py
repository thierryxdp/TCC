def inverte(x=""):
	'''
    '''
    x=x.replace(".","").replace(";"," ").replace(",","").replace("!","").replace("?"," ").replace("-","").replace("/","").replace(":","").lower()
    x=x.split(" ")
    return str(" ").join(x[::-1])