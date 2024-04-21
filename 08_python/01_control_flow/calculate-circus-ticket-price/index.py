def calculate_ticket_price_for_performer(regular_ticket_price, performer_type):
   if performer_type == 'Juggler':
      ticket_price = regular_ticket_price * 0.5
   elif performer_type == 'Fire Twirler':
      ticket_price = regular_ticket_price * 0.75
   elif performer_type == 'Magician':
      ticket_price = regular_ticket_price * 0.2
   elif performer_type == 'Escape Artist':
      ticket_price = 0
   else:
      ticket_price = regular_ticket_price * 0.8
   return ticket_price

ticket_price = calculate_ticket_price_for_performer(100, "Juggler")
print(ticket_price)
ticket_price = calculate_ticket_price_for_performer(200, "Magician")
print(ticket_price)
ticket_price = calculate_ticket_price_for_performer(10, "Tight Rope Walker")
print(ticket_price)
ticket_price = calculate_ticket_price_for_performer(150, "Escape Artist")
print(ticket_price)
