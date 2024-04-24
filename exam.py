class Star_cinema:
        hall_list=[]
        def entry_hall(self,hall):
            Star_cinema.hall_list.append(hall)

class Hall(Star_cinema):
    def __init__(self,rows,cols,hall_no):
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.__hall_no=hall_no

    def entry_show(self,id, movie_name,time):
        show=(id, movie_name,time)
        self.show_list.append(show)
        seatAvailable=[]
        for row in range(self.rows):
            rowInfo=[]
            for col in range(self.cols):
                rowInfo.append(True)
            seatAvailable.append(rowInfo)
            self.seats[id]=seatAvailable

    def book_seats(self, show_id, seat_list):
            for show in self.show_list:
                if show[0] == show_id:
                    available_seats = self.seats[show_id]
                    for seat in seat_list:
                        row, col =[int (val) for val in seat]
                        if 0 < row <= self.rows and 0 < col <= self.cols:
                            if available_seats[row - 1][col - 1]:
                                print(f"Seat {seat} booked successfully!")
                                available_seats[row - 1][col - 1] = False
                            else:
                                print(f"Seat {seat} is already booked.")
                                return
                        else:
                            print(f"Seat {seat} is invalid.")
                            return
                    return
                else:
                    print("Invalid show ID.")

    def view_show_list(self):
        for show in self.show_list:
            print(f"Movie Name:{show[1]} Showid:{show[0]} Time: {show[2]}")

    def view_available_seats(self, show_id):
        for show in self.show_list:
            if show[0]==show_id:
                available_seats = self.seats[show_id]
                if available_seats:
                    print("Available Seats:")
                    for row in range(self.rows):
                        for col in range(self.cols):
                            if available_seats[row][col]:
                                print(f"seat: ({row + 1},{col + 1})")
                return
        print("Invalid show ID.")
    
cinema=Hall(11,16,18)
star_cinema=Star_cinema()
star_cinema.entry_hall(cinema)
cinema.entry_show(3,"kgf chapter1"," 11-04-2024 9:00PM")
cinema.entry_show(7,"kgf chapter2","11-04-2024 11:00AM")

while True:
    print("Welcome to cinema hall.Enter option")
    print("1. View all show today")
    print("2. View available seats")
    print("3. Book ticket")
    print("4. Exit")

    ch=int(input("Enter option: "))
    if(ch==1):
        cinema.view_show_list()
    elif(ch==2):
        show_id=int(input("enter show id: "))
        cinema.view_available_seats(show_id)
    elif(ch==3):
        show_id=int(input("Enter show id: "))
        seat_list=[]
        row=input("Enter row number: ")
        col=input("Enter col number: ")
        seat_list.append((row,col))
        cinema.book_seats(show_id, seat_list)
    elif(ch==4):
        print("Exit succesfully.Thanks your visiting.")
        break
    else:
        print("Invalid option")