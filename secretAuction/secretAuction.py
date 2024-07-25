from art import logo

print(logo)

bids = {}

def add_bid(name, bid):
    if name in bids:
        bids[name].append(bid)
    else:
        bids[name] = [bid]

while True:
    name = input("Please enter your name: ")
    bid = float(input("Please enter your bid:$ "))
    add_bid(name, bid)
    
    more_bids = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bids == 'no':
        break

highest_bid = 0
highest_bidder = ""

for name, bid_list in bids.items():
    for bid in bid_list:
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = name

print(f"The highest bid is ${highest_bid} by {highest_bidder}")
