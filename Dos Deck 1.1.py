import random


def deckBuild():
    deck = []
    colours = ["Red", "Green", "Yellow", "Blue"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
    wilds = ["wild", "Dos"]
    for colour in colours:
        for number in numbers:
            cardvalue = '{} {}'.format(colour, number)
            deck.append(cardvalue)
            if number < 6:
                deck.append(cardvalue)
                deck.append(cardvalue)
            elif number > 5:
                deck.append(cardvalue)
    for i in range(8):
        deck.append(wilds[0])
    for i in range(12):
        deck.append(wilds[1])
    return deck


def shuffleDeck(deck):
    for cardSpace in range(len(deck)):
        randomSpace = random.randint(0, 107)
        deck[cardSpace], deck[randomSpace] = deck[randomSpace], deck[cardSpace]
    return deck


def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(dosDeck.pop(0))
    return cardsDrawn


def myHand(player, playerHand):
    print("player {}'s Move".format(player + 1))
    print("My hand: ")
    print("-------")
    y = 1
    for card in playerHand:
        print("{} {} ".format(y, card))
        y += 1
    print("")


def validPlay(colour, number, playerHand):
    for card in playerHand:
        splitCard = card.split(' ', 1)
        if "Wild" in splitCard[0]:
            return True
        elif colour in card or number in card:
            return True
    return False


dosDeck = deckBuild()
dosDeck = shuffleDeck(dosDeck)
dosDeck = shuffleDeck(dosDeck)
discards = []
print(dosDeck)

players = []
numPlayers = int(input("1 or 2 players? "))
while numPlayers < 0 or numPlayers > 3:
    numPlayers = int(input("1 or 2 players? "))
for player in range(numPlayers):
    players.append(drawCards(7))

playerTurn = 0
playerDirect = 1
playing = True
discards.append(dosDeck.pop(0))
splitCard = discards[0].split(" ", 1)
currentColour = splitCard[0]
if currentColour != "Wild":
    cardVal = splitCard[1]
else:
    cardVal = "Any"

while playing:
    myHand(playerTurn, players[playerTurn])
    print("Most recent discard is: {}".format(discards[-1]))
    if validPlay(currentColour, cardVal, players[playerTurn]):
        chooseCard = int(input("Which card will you play? "))
        while not validPlay(currentColour, cardVal, [players[playerTurn][chooseCard - 1]]):
            chooseCard = int(input("Oops, can't play that one. Which card will you play? "))
        print("Played {}".format(players[playerTurn][chooseCard-1]))
        print("")
        discards.append(players[playerTurn].pop(chooseCard - 1))
    else:
        print(" No valid plays. Please draw a card.")
        players[playerTurn].extend(drawCards(1))
    playerTurn += playerDirect
    if playerTurn == numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers - 1

    





