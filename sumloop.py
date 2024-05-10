def card_rank(card):
    face_cards = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    if card.isdigit():
        return int(card)
    else:
        return face_cards[card]
cards = []
for _ in range(6):
    card = input().strip().capitalize()
    cards.append(card)
total_rank = sum(card_rank(card) for card in cards)
average_rank = total_rank / len(cards)
print(average_rank)
