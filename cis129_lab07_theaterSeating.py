#First step to creating this code will be to set the variables, since pricing can change we want to make it as clear as possible and as easy as possible to change them.

cost_section_a = 20
cost_section_b = 15
cost_section_c = 10

#This also allows for easy implementation of new sections
#Next we need to state the seat counts in each section, as well as make it easy for the section to add and remove seats in each section

seat_a = 300
seat_b = 500
seat_c = 200

#We now need an input for each number of tickets sold in each section.
#These numbers will be intergers because it is impossible to sell half a seat.

ticket_a = int(input('Ticket sales for section A: '))
ticket_b = int(input('Ticket sales for section B: '))
ticket_c = int(input('Ticket sales for section C: '))

#Now to validate our inputs. To do this we must compare the inputed ticket sales with the total number of seats, as well as confirming that the number is not a negative for each section.

if(ticket_a < 0 or ticket_a > seat_a):
    print('Section A sales must be between 0 and ' + str(seat_a))
elif(ticket_b < 0 or ticket_b > seat_b):
    print('Section B sales must be between 0 and ' + str(seat_b))
elif(ticket_c < 0 or ticket_c > seat_c):
    print('Section C sales must be between 0 and ' + str(seat_c))
else:
    income_a = ticket_a * cost_section_a
    income_b = ticket_b * cost_section_b
    income_c = ticket_c * cost_section_c
    income_total = income_a + income_b + income_c
    
    print('Income generated from section A: $' + str(income_a))
    print('Income generated from section B: $' + str(income_b))
    print('Income generated from section C: $' + str(income_c))
    print('Total income generated from ticket sales: $' + str(income_total))

#If all seat values are verified and possible, then the program will output the the profits from each section and the total profits.
