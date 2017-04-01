
def URLgen(model, size):
	baseSize = 580

	shoeSize = size - 6.5
	shoeSize = shoeSize * 20
	rawSize = shoeSize + baseSize
	shoeSizeCode = int(rawSize)
	URL = 'http://www.adidas.com/us/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(shoeSizeCode)
	return URL

model = raw_input('Model #')
size = input('Size: ')
URL = URLgen(model, size)
print (str(URL))