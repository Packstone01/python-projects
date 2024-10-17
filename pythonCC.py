pizzas = ['pepperoni', 'cheese', 'three meat']

for pizza in pizzas:
  print(f'{pizza.title()} is good!')

print('Those are some of my favorites!')

animals = ['tiger', 'lion', 'panther']

for animal in animals:
  print(f'{animal.title()} would not make a good pet.')

print('The common trait between them is that they are all cats!')

for value in range(6):
  print(value)

numbers = list(range(1,6))
print(numbers)

evenNumbers = list(range(2,11,2))
print(evenNumbers)

squares = []
for value in range(1,11):
  squares.append(value ** 2)

print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)


digits = [1, 2, 3, 4, 5,6, 7, 8, 9, 0]
print(min(digits))
print(sum(digits))

# Count to twenty
for num in range(1,21):
  print(num)

# One million
# for num in range(1,1000001):
#   print(num)

# Summing a million
sumMil = []
for value in range(1,1000001):
  sumMil.append(value)
print(min(sumMil))
print(max(sumMil))
print(sum(sumMil))

# Odd numbers
odd = []
for num in range(1,21,2):
  odd.append(num)
print(odd)

# Threes
three = []
for num in range(3,21,3):
  three.append(num)
print(three)

# Cubes
cubes = []
for num in range(1,11):
  cubes.append(num ** 3)
print(cubes)

# Cube comprehension
cube = [num ** 3 for num in range(1,11)]
print(cube)

players = ['connor', 'lexy', 'heather', 'kelly', 'mother', 'father']
print(players[1:2])

print('Here is everyone:')
for player in players[:3]:
  print(player.title())

buffets = ('nuggets', 'pasta', 'fries', 'wings', 'veggies')
for buffet in buffets:
  print(buffet.title())
