def afd(total_money, price_per_piece):
    num_pieces = total_money // price_per_piece
    left = total_money - price_per_piece*num_pieces
    return f"you can afford {num_pieces} piece(s) of chocolate bar. And you still have {left} dollars left."

#Example
print("example:")
total_money = 100
price_per_piece = 7
print(f"Based on the information that you have {total_money} dollars in total and each piece of chocolate bar costs {price_per_piece} dollars, so {afd(total_money, price_per_piece)}")
#the output is "Based on the information that you have 100 dollars in total and each piece of chocolate bar costs 7 dollars, so you can afford 14 pieces of chocolate bar. And you still have 2 dollars left."