products = []
while True:
	name = input('Please enter the products name:')
	if name == 'q':
		break

	price = input('Please enter the products price:')
	#p = []
	#p.append(name)
	#p.append(price)
	#p = [name, price]
	#products.append(p)
	products.append([name, price])

print(products)

print(products[0][0])

for p in products:
	print(p[0], 'is', p[1])