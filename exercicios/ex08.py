
print('########### - Exercicios 08- #############')
n=1
resposta ='Inicial'
while resposta != 's':
    resposta = input(f'Vamo{"o"*n} sair hoje [s/n]:  ')
    n+=1
    if 'chato' in resposta:
        print('Foi mal')
        break
else:
    print(f'Então vamo{"o"*n}')
