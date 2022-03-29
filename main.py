import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
result = reader.readtext('C:\Users\Roopa\Pictures\Camera Roll\raw.png')