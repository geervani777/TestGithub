import goslate
 
text = "Hello World"
 
gs = goslate.Goslate()
translatedText = gs.translate('hello','hi')
 
print(translatedText)
