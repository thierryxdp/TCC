def lingua_p(string):
    for vogal in "aáeéiouú":
    	string = str.replace(string,vogal,vogal + "p" + vogal)
    return string