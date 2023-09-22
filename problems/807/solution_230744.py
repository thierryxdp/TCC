def conta_frases(text):
 
  text = text.replace(".","\n")
  text = text.replace("?","?\n")
  text = text.replace("!","!\n")
  sentences = text.split("\n")
  # sentences = sentences[:-1]
    # sentences = [s.strip() for s in sentences]
  return sentences