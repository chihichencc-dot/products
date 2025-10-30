import os

def read_file(filename):
	products = []
	with open (filename, 'r') as f:
			for line in f:
				if 'Item,Price' in line:
					continue
				name, price = line.strip().split(',')
				products.append([name, price])
	return products

def user_input(products):
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
	return products

def print_products(products):
	for p in products:
		print(p[0], 'is', p[1])

def write_file(filename, products):
	with open(filename, 'w') as f:
		f.write('Item,Price\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('yes, file found!')
		products = read_file(filename)
	else:
		print('nope!')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()

#refactor