from greetings import greetings

print('What\'s your name?')
n = input()
g = Greetings(n)
print(g.say_hi())
