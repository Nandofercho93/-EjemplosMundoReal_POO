def display_ticket_options():
    print("-------------------------------------------------------")
    print("Entradas:")
    print("1. General - $10")
    print("2. Tribuna - $15")
    print("3. Palco - $50")
    print("-------------------------------------------------------")

def get_ticket_details():
    ticket_type = int(input("Ingrese la preferencia (1, 2, or 3): "))
    number_of_tickets = int(input("Ingrese numero de entradas: "))
    return ticket_type, number_of_tickets

def calculate_total_cost(ticket_type, number_of_tickets):
    if ticket_type == 1:
        price_per_ticket = 10
    elif ticket_type == 2:
        price_per_ticket = 15
    else:
        price_per_ticket = 50

    total_cost = price_per_ticket * number_of_tickets
    return total_cost

def assign_seats(ticket_type, number_of_tickets):
    seats = []
    for i in range(1, number_of_tickets + 1):
        if ticket_type == 1:
            seat_type = "General"
        elif ticket_type == 2:
            seat_type = "Tribuna"
        else:
            seat_type = "Palco"

        seat_number = f"{seat_type} - {i}"
        seats.append(seat_number)

    return seats

def display_ticket_information(seats, total_cost):
    print("-------------------------------------------------------")
    print("Informacion entrada:")
    for seat in seats:
        print(f"Seat: {seat}")
    print(f"Total Cost: ${total_cost}")
    print("-------------------------------------------------------")

def main():
    while True:
        display_ticket_options()
        ticket_type, number_of_tickets = get_ticket_details()
        total_cost = calculate_total_cost(ticket_type, number_of_tickets)
        seats = assign_seats(ticket_type, number_of_tickets)
        display_ticket_information(seats, total_cost)

        choice = input("Quiere realizar otra reserva de entrada (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()
