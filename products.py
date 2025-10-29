import os

products = []
if os.path.isfile('products.csv'):
	print('yes, file found!')
	with open ('products.csv', 'r') as f:
		for line in f:
			if 'Item,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)

else:
	print('nope!')
#check if there is such file in the same path





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

#print(products[0][0])

for p in products:
	print(p[0], 'is', p[1])

with open('products.csv', 'w') as f:
	f.write('Item,Price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')