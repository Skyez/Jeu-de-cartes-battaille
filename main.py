from random import shuffle
from utils.determine_winner import determine_winner
from utils.equality import equality

cards = ["As ♦️", "2 ♦️", "3 ♦️", "4 ♦️", "5 ♦️", "6 ♦️", "7 ♦️", "8 ♦️", "9 ♦️", "10 ♦️", "Vallet ♦️", "Dame ♦️", "Roi ♦️",
		"As ♠️", "2 ♠️", "3 ♠️", "4 ♠️", "5 ♠️", "6 ♠️", "7 ♠️", "8 ♠️", "9 ♠️", "10 ♠️", "Vallet ♠️", "Dame ♠️", "Roi ♠️",
		"As ♥️", "2 ♥️", "3 ♥️", "4 ♥️", "5 ♥️", "6 ♥️", "7 ♥️", "8 ♥️", "9 ♥️", "10 ♥️", "Vallet ♥️", "Dame ♥️", "Roi ♥️",
		"As ♣️", "2 ♣️", "3 ♣️", "4 ♣️", "5 ♣️", "6 ♣️", "7 ♣️", "8 ♣️", "9 ♣️", "10 ♣️", "Vallet ♣️", "Dame ♣️", "Roi ♣️"]

shuffle(cards)

cards_player_one = cards[:len(cards)//2]
cards_player_two = cards[len(cards)//2:]
count = 0

while True:
	try:
		count += 1
		card_player_one = cards_player_one[0]
		card_player_two = cards_player_two[0]

		winner = determine_winner(card_player_one, card_player_two)
		if not winner == "equal":
			if winner == card_player_one:
				cards_player_one.remove(card_player_one)
				cards_player_two.remove(card_player_two)

				cards_player_one.append(card_player_one)
				cards_player_one.append(card_player_two)
			else:
				cards_player_two.remove(card_player_two)
				cards_player_one.remove(card_player_one)

				cards_player_two.append(card_player_one)
				cards_player_two.append(card_player_two)

			input(f"""

Joueur 1: {card_player_one}
Joueur 2: {card_player_two}

{'Joueur 1' if winner == card_player_one else 'Joueur 2'} a gagné !
Le Joueur 1 a {len(cards_player_one)} cartes.
Le Joueur 2 a {len(cards_player_two)} cartes.
""")

		else:
			cards_to_win = []
			battle_player_one = []
			battle_player_two = []
			input(f"""

Joueur 1: {card_player_one}
Joueur 2: {card_player_two}

Il y a égalité
""")

			equality(cards_player_one, cards_player_two, card_player_one, card_player_two, cards_to_win, battle_player_one, battle_player_two)

	except:
		input(f"""
Partie Terminée !

{'Joueur 1' if not len(cards_player_one) == 0 else 'Joueur 2'} a gagné la partie !

Il y a eu {count} coups !
""")
		exit()