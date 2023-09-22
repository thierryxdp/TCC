def inverte(frase: str) -> str:
    palavras = frase.replace(".", "")\
				    .replace(",", "")\
				    .replace(":", "")\
				    .replace(";", "")\
    			    .replace("?", "")\
        		    .replace("!", "")\
				    .replace("-", "")\
				    .split(" ")
    return reversed(palavras)