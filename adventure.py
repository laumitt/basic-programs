print('Welcome to The Most Awesome Text Adventure Game.')
print('What is your name?')
playerName = input()
print('Hello ' + playerName)
print('Type START to begin.')
start = input()
while start:
    if start == 'START':
        print('Beginning The Most Awesome Text Adventure Game...')
        break
    else:
        print('Invalid response. Type START to begin.')
        start = input()
print('It was a dark and stormy night...')
print('Jk it was a nice sunny day, about 3:30, and you were walking to the train.')
print('You were waiting to cross the street. The light was red but no cars were coming.')
print('Do you JAYWALK or WAIT?')
crossChoice = input()
while crossChoice:
    if crossChoice == 'JAYWALK':
        print('You cross the street quickly, ignoring the red hand.')
        print('Naturally as soon as you get to the other side the signal changes to walk.')
        break
    elif crossChoice == 'WAIT':
        print('You wait for the light to change, which it does fairly quickly.')
        print('You cross the street and carry on down the block.')
        break
    else:
        print('Invalid choice. Please try again.')
        print('Do you JAYWALK or WAIT?')
        crossChoice = input()
print('At the next intersection, you find a shiny object on the ground.')
print('Do you PICK IT UP or KEEP WALKING?')
keyChoice = input()
while keyChoice:
    if keyChoice == 'PICK IT UP':
        print('You pick up the key and put it in your pocket.')
        break
    elif keyChoice == 'KEEP WALKING':
        print('You ignore it and keep walking. Behind you you hear a hissing noise.')
        print('You turn back and see a stream of smoke rising from the cracks in the sidewalk around the key.')
        print('The sidewalk explodes and the key flies into your hand anyway.')
        break
    else:
        print('Invalid choice. Please try again.')
        print('Do you PICK IT UP or KEEP WALKING?')
        keyChoice = input()
