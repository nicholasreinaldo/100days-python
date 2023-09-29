from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program.")

bid_pool = []


def new_bid(input_name, input_bid):
    new_bidder = {
        "bidder_name": input_name,
        "bid_amount": input_bid,
    }
    bid_pool.append(new_bidder)


bidding = True
while bidding:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    more_bidders = input("Are there any other bidders? Type 'yes or no' \n")
    new_bid(input_name=name, input_bid=bid)
    if more_bidders == "no":
        bidding = False
        bid_amounts = []
        for bidder in bid_pool:
            bid_amounts.append(bidder["bid_amount"])
        highest_bid_amount = max(bid_amounts)
        highest_bidder_name = bid_pool[bid_amounts.index(highest_bid_amount)]["bidder_name"]
        print(f"The winner is {highest_bidder_name} with a bid of ${highest_bid_amount}")
    elif more_bidders == "yes":
        clear()

print(bid_pool)