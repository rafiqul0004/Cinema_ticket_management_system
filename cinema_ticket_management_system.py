class Star_Cenema:
    def __init__(self):
        self.hall_list = []

    def entry_hall(self, rows, cols, hall_no):
        hall = Hall(rows, cols, hall_no)
        self.hall_list.append(hall)


class Hall(Star_Cenema):
    def __init__(self,rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().__init__()

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        seats = [[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seats

    def book_ticket(self, show_id, seats):
        if show_id not in self.__seats:
            print(f'Show is only available for {show_id}')
            print("Show is unavailable for other hall")
        else:
            seat = self.__seats[show_id]
            for row, col in seats:
                if 1 <= row <= self.__rows and 1 <= col <= self.__cols:
                    if seat[row - 1][col - 1] == 0:
                        seat[row - 1][col - 1] = 1
                        print("Your seat is booked successfully")
                        for i in range(self.__rows):
                            for j in range(self.__cols):
                                print(seat[i][j], end=' ')
                            print()
                    else:
                        print("Seat is already booked")
                else:
                    print("Invalid seat")

    def view_show_list(self):
        return self.__show_list

    def available_seats(self, show_id):
        if show_id not in self.__seats:
            print(f'Show is only available for {show_id}')
            print("Show is not avaiable for others hall")
        else:
            seat = self.__seats[show_id]
            for i in range(self.__rows):
                for j in range(self.__cols):
                    print(seat[i][j], end=' ')
                print()

hall1 = Hall(4, 4, 100)
hall2 = Hall(5, 5, 101)
star = Star_Cenema()
star.entry_hall(4, 4, 100)
star.entry_hall(5, 5, 101)
hall1.entry_show(100, 'Jawan[100]', '11:00')
hall2.entry_show(101, 'Sujan maji[101]', '12:00')

while True:
    print("1.Show List")
    print("2.Seat Available")
    print("3.Book Seat")
    print("4.Exit")
    ch = int(input("\nEnter an option: "))
    if ch == 1:
        show_list = hall1.view_show_list() + hall2.view_show_list()
        print("Show List:")
        for show in show_list:
            print(show)
    elif ch == 2:
        p = int(input("\nEnter The show id: "))
        hall1.available_seats(p)
        hall2.available_seats(p)
    elif ch == 3:
        p = int(input("\nEnter The show id: "))
        k = int(input("\nEnter The number of tickets: "))
        while k>0:
            r = int(input("\nEnter The row number: "))
            c = int(input("\nEnter The column number: "))
            seat = [(r, c)]
            hall1.book_ticket(p, seat)
            hall2.book_ticket(p, seat)
            k-=1
    elif ch == 4:
        print("Thanks for visiting")
        break
    else:
        print("Please provide a valid option")