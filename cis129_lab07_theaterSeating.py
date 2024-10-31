cost_section_a = 20
cost_section_b = 15
cost_section_c = 10

seat_a = 300
seat_b = 500
seat_c = 200

ticket_a = int(input('Ticket sales for section A: '))
ticket_b = int(input('Ticket sales for section B: '))
ticket_c = int(input('Ticket sales for section C: '))

if(ticket_a < 0 or ticket_a > seat_a):
    print('Section A sales must be between 0 and ' + str(seat_a))
elif(ticket_b < 0 or ticket_b > seat_b):
    print('Section B sales must be between 0 and ' + str(seat_b))
elif(ticket_c < 0 or ticket_c > seat_c):
    print('Section C sales must be between 0 and ' + str(seat_c))
else:
    income = (ticket_a * cost_section_a) + (ticket_b * cost_section_b) + (ticket_c * cost_section_c)
    print('Total income generated from ticket sales: $' + str(income))
