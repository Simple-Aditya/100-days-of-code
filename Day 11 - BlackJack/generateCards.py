from pprint import pformat

def make_card(rank, suit):
    """
    Creates an ASCII representation of a single playing card.

    Args:
        rank (str): The rank of the card ('2'-'10', 'J', 'Q', 'K', 'A').
        suit (str): The suit of the card ('♠', '♥', '♦', '♣').
    """
    top = "┌─────────┐"
    bottom = "└─────────┘"
    side = "│         │"

    if rank == "10":  # Ten is the only rank with two digits
        rank_right = rank
        rank_left = rank
    else:
        rank_right = rank + " "
        rank_left = " " + rank

    suit_line = f"│    {suit}    │"
    rank_line_left = f"│{rank_left}       │"
    rank_line_right = f"│       {rank_right}│"

    return top + '\n' + rank_line_left + "\n" + side + "\n" + suit_line + "\n" + side + "\n" + rank_line_right + "\n" + bottom


def main():
    cards = {}
    for i in range(2, 13):
        rank = str(i) if i < 10 else ["J", "Q", "K", "A"][i - 10]
        for suit in ['♠', '♥', '♦', '♣']:
             cards[f"{rank}_{suit}"] = make_card(rank, suit)
    
    with open("cards.py", "w", encoding="utf-8") as f:
        f.write("cards = ")
        f.write(pformat(cards))
    

if __name__ == "__main__":
    main()