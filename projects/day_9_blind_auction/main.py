# from replit import clear
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
    more_bidders = input("Are there any other bidders? Type 'yes or no'"))
    new_bid(input_name=name, input_bid=bid)
    if more_bidders == "no":
        bidding = False
        print(f"The winner is {} with a bid of ${}")

