print('########### - comprar o mais barato - #############')

preco_1 = float(input('Preço 1:  '))
preco_2 = float(input('Preço 2:  '))
preco_3 = float(input('Preço 2:  '))

if preco_1 > preco_2 and preco_2 > preco_3:
    print('Compre o produto 3')
elif preco_2 > preco_1 and preco_1 < preco_3:
    print('Compre o produto 1')
else:
    print('Compre o produto 2')
