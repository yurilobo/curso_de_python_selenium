print('########### - Boletim - #############')

nota_1 = float(input('Digite sua primeira nota:  '))
nota_2 = float(input('Digite sua segunda nota:  '))
media =(nota_1+nota_2)/2
if media == 10:
    print(f'Sua media foi {media}, e você está APROVADO COM DISTINÇÃO')
elif media >= 7 and media<10:
    print(f'Sua media foi {media}, e você está APROVADO')
else:
    print(f'Sua media foi {media}, e você está REPROVADO')
