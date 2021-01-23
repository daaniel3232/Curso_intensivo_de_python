lista = ['Daniel', 'Monica', 'Walter']
print('{}, {}, {} encontramos uma mesa maior!'.format(lista[0], lista[1], lista[2]))
lista.insert(0, 'Jonas')
lista.insert(2, 'Raquel')
lista.append('Rubens')
print('Agora são {} convidados para a festa'.format(len(lista)))
lista.sort()
print('Eles são {}, {}, {}, {}, {}, {}'.format(lista[0], lista[1], lista[2], lista[3], lista[4],lista[5]))


