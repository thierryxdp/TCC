def lingua_p(string):
    for vogal in "aeiou":
    	string = str.replace(string,vogal,vogal + "p" + vogal)
    return string