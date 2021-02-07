pizzas = ['queijo', 'portuguesa', 'mista', '4 queijos', 'frango']
friend_pizzas = pizzas[:]
pizzas.append('calabresa')
friend_pizzas.append('banana')

for minha in pizzas:
    print("Minhas pizzas favoritas são: "+minha.title())

for friends in friend_pizzas:
    print("As pizzas favoritas dos meus amigos são: "+friends.title())