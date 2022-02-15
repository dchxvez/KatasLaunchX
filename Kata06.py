planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print('There are', len(planets), 'planets')
planets.append('Pluto') #add new objet 
print(planets[-1], 'is the last planet')#Last character

#Second excersice

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
print('Please chose the name of one planet amoung the following list')
print(planets)
user_planet = input('Enter your planet (with a capital letter to start)')
planet_index = planets.index(user_planet)
print('Here are the planets closer than ' + user_planet)
print(planets[0:planet_index])
print('Here are the planets further than ' + user_planet)
print(planets[planet_index + 1:])