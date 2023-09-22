def inverte(frase: str) -> str:
    palavras = frase.replace(".", "")\
				    .replace(",", "")\
				    .replace(":", "")\
				    .replace(";", "")\
    			    .replace("?", "")\
        		    .replace("!", "")\
				    .replace("-", "")\
				    .split(" ")
    return str.join(" ", reversed(palavras)).lower()