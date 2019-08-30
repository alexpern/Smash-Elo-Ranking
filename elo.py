import argparse
import os.path
import json

parser = argparse.ArgumentParser()
parser.add_argument('--player1', required=True, help='name of player 1')
parser.add_argument('--player2', required=True, help='name of player 2')
parser.add_argument('--winner', required=True, help='name of winner')
args = parser.parse_args()

a = args.player1
b = args.player2
winner = args.winner

if not os.path.exists('playerDB.json'):
	blankDict = {}
	dictFile = open('playerDB.json', 'w')
	json.dump(blankDict, dictFile)

dbFile = open('playerDB.json', 'r')
playerDB = json.load(dbFile)

if a not in playerDB:
	playerDB[a] = 0
if b not in playerDB:
	playerDB[b] = 0

ratingA = playerDB[a]
ratingB = playerDB[b]

expectedA = 1/(1 + (10 ** ((ratingB - ratingA) / 400)))
expectedB = 1 - expectedA

if winner == a:
	actualA = 1
	actualB = 0
elif winner == b:
	actualA = 0
	actualB = 1
else:
	raise Exception('invalid winner entered')

k = 16

newRatingA = ratingA + (k * (actualA - expectedA))
playerDB[a] = newRatingA
newRatingB = ratingB + (k * (actualB - expectedB))
playerDB[b] = newRatingB
print(a + ' new rating: ' + str(newRatingA))
print(newRatingA - ratingA)
print(b + ' new rating: ' + str(newRatingB))
print(newRatingB - ratingB)

dbFile.close()

dbWriter = open('playerDB.json', 'w')
newDict = json.dump(playerDB, dbWriter)
print(playerDB)
dbWriter.close()

# if two unranked players play, they each have a 50% chance of winning (expectedA = .5)
# Player A wins, and is not a topPlayer
# newRating = 0 + (16 * (1 - .5))
# newRating = 8
# newRatingB = 0 + (16 * (0 - .5))
# newRatingB = -8

# They play again for game 2
# expectedA = 1/1 + (10 ** ((-8 - 8) / 400))
# expectedA = .523
# expectedB = .477
# PlayerA wins again
# newRating = 8 + (16 * (1 - .523))
# newRating = 15.632
# newRatingB = -8 + (16 * (0 - .477))
# newRatingB = -15.632

# Match 2:
# Player A plays another new player who got a bye
# expectedA = 1 / (1 + (10 ** ((0 - 15.632) / 400)))
# expectedA = .522
# expectedB = .476
# Player A wins
# newRating = 15.632 + (16 * (1 - .522))
# newRating = 23.28
# newRatingB = 0 + (16 * (0 - .476))
# newRatingB = -7.616

# Game 2
# expectedA = 1 / (1 + (10 ** ((-7.616 - 23.28) / 400)))
# expectedA = .544
# expectedB = .456
# Player A wins
# newRating = 23.28 + (16 * (1 - .544))
# newRating = 30.576
# newRatingB = -7.616 + (16 * (0 - .4560-))
# newRatingB = -14.912