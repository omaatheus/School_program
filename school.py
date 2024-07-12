media1 = float(input('Escreva a primeira nota do Aluno: '))
media2 = float(input('Escreva a segunda nota do Aluno: '))

mediaCalculada = (media1 + media2) / 2

mediaCorreta = float(f'{mediaCalculada:.1f}')

# if (mediaCorreta >= 7):
#     print(f'Parabéns, sua nota foi de {mediaCorreta} e você passou!')
# else:
#     print(f'Sua nota foi de {mediaCorreta} e infelizmente você ficou retido.')
    
if (mediaCorreta < 4):
    print(f'Você está retido, sua nota foi de: {mediaCorreta}')
else:
    if((mediaCorreta >= 4) and (mediaCorreta < 7)):
        print(f'Você ficou de recuperação, sua nota foi de: {mediaCorreta}')
    else:
        if ((mediaCorreta >= 7) and (mediaCorreta <= 10)):
            print(f'Parabéns, você foi aprovado com nota de: {mediaCorreta}')
