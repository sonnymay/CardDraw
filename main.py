import requests
import json

def shuffle_deck():
    response = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
    if response.status_code == 200:
        deck_id = response.json()['deck_id']
        return deck_id
    else:
        return None
    
def draw_card(deck_id):
    response = requests.get(f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=1")
    if response.status_code == 200:
        card = response.json()['cards'][0]
        return card
    else:
        return None
    
def main():
    deck_id = shuffle_deck()
    if deck_id is None:
        print("Error: Could not shuffle deck")
        return
    
    card = draw_card(deck_id)
    if card is None:
        print("Error: Could not draw card")
        return
    
    print(f"Your card is the {card['value']} of {card['suit']}")

if __name__ == "__main__":
    main()