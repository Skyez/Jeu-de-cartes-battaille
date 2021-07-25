from .determine_winner import determine_winner

def equality(cards_player_one, cards_player_two, card_player_one, card_player_two, cards_to_win, battle_player_one, battle_player_two):
	cards_player_one.remove(card_player_one)
	cards_player_two.remove(card_player_two)

	hide_card_player_one = cards_player_one[0]
	hide_card_player_two = cards_player_two[0]

	input(f"""
Joueur 1: Carte Cachée
Joueur 2: Carte Cachée
""")

	cards_player_one.remove(hide_card_player_one)
	cards_player_two.remove(hide_card_player_two)

	new_card_player_one = cards_player_one[0]
	new_card_player_two = cards_player_two[0]

	cards_to_win.append(hide_card_player_one)
	cards_to_win.append(hide_card_player_two)
	cards_to_win.append(new_card_player_one)
	cards_to_win.append(new_card_player_two)
	cards_to_win.append(card_player_one)
	cards_to_win.append(card_player_two)

	battle_player_one.append(card_player_one)
	battle_player_one.append(hide_card_player_one)
	battle_player_one.append(new_card_player_one)

	battle_player_two.append(card_player_two)
	battle_player_two.append(hide_card_player_two)
	battle_player_two.append(new_card_player_two)

	winner = determine_winner(new_card_player_one, new_card_player_two)

	if not winner == "equal":
		cards_player_one.remove(new_card_player_one)
		cards_player_two.remove(new_card_player_two)
		if winner == new_card_player_one:
			for card in cards_to_win:
				cards_player_one.append(card)
		else:
			for card in cards_to_win:
				cards_player_two.append(card)
		input(f"""
Joueur 1: {new_card_player_one}
Joueur 2: {new_card_player_two}

{'Joueur 1' if winner == new_card_player_one else 'Joueur 2'} a gagné !
Le Joueur 1 a {len(cards_player_one)} cartes.
Le Joueur 2 a {len(cards_player_two)} cartes.

Carte dans la bataille du Joueur 1: {', '.join(battle_player_one)}
Carte dans la bataille du Joueur 2: {', '.join(battle_player_two)}
""")

	else:
		input(f"""

Joueur 1: {new_card_player_one}
Joueur 2: {new_card_player_two}

Il y a égalité
""")
		return equality(cards_player_one, cards_player_two, new_card_player_one, new_card_player_two, cards_to_win, battle_player_one, battle_player_two)