import random


# Making the draw:
def draw(participants):
    drawn = []  # List of drawn people:

    participantsSize = len(participants)
    while len(drawn) < participantsSize:
        randomIndex = random.randrange(len(participants))   # Sorting random number, inside participants length. Ref: https://docs.python.org/3/library/random.html#random.seed
        drawn.append(participants[randomIndex])             # Putting person in the drawn list.
        participants.remove(participants[randomIndex])      # Removing person from participants list, to not be drawn again (by him/herself or closing the circle beforehand).

    drawn.append(drawn[0])  # Closing circle.

    #print('Drawn list: ' + ' -> '.join(drawn))
    return drawn
