lista = ['Daniel', 'Monica', 'Walter']
print('{} não poderá comparecer'.format(lista[0]))
lista.insert(0, 'Joaquim')
lista.remove('Daniel')
print('{} você está convidado a participar da festa\n'
      '{} você está convidado a participar da festa\n'
      '{} você está convidado a participar da festa\n'.format(lista[0], lista[1], lista[2]))
