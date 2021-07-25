def determine_winner(card_one, card_two):
	cards = [card_one, card_two]
	cards_type = []

	for card in cards:
		try:
			card = int(card[0])
		except:
			if card.startswith("As"):
				card_type = 14
				cards_type.append(card_type)

			elif card.startswith("Vallet"):
				card_type = 11
				cards_type.append(card_type)

			elif card.startswith("Dame"):
				card_type = 12
				cards_type.append(card_type)

			elif card.startswith("Roi"):
				card_type = 13
				cards_type.append(card_type)
			
		else:
			card_type = card
			cards_type.append(card_type)

	if cards_type[0] > cards_type[1]:
		return card_one

	elif cards_type[0] < cards_type[1]:
		return card_two

	elif cards_type[0] == cards_type[1]:
		return "equal"