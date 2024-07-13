import datetime
x=datetime.datetime.now()
class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Showtime:
    def __init__(self, movie, time):
        self.movie = movie
        self.time = time
        self.seats = [True] * 50  

    def book_seat(self, seat_number):
        if self.seats[seat_number]:
            self.seats[seat_number] = False
            return True
        else:
            return False

class BookingSystem:
    def __init__(self):
        self.movies = []
        self.showtimes = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def add_showtime(self, showtime):
        self.showtimes.append(showtime)

    def display_movies(self):
        for i, movie in enumerate(self.movies):
            print(f"{i + 1}. {movie.title} ({movie.duration} mins)")

    def display_showtimes(self):
        for i, showtime in enumerate(self.showtimes):
            print(f"{i + 1}. {showtime.movie.title} at {showtime.time}")

    def book_ticket(self, showtime_index, seat_number):
        showtime = self.showtimes[showtime_index]
        if showtime.book_seat(seat_number):
            if showtime.movie.title == "THE PURSUIT OF HAPPYNESS":
                print(f"""Booking successful for THE PURSUIT OF HAPPYNESS
                -------------------------------------------------------------------
                THE PURSUIT OF HAPPYNESS                                                               
                U/A ENGLISH 2D                                                            
                TPV Multiplex 3D 4k Dolby Atmos
                ----------------SCAN QR CODE AT CINEMA----------------
                Screen 1 Dolby Atmos,03:00 PM
                Seat Number:{seat_number}
                Booking Date and Time:{x}
                Booking Code:HWKBSOGW
                Booking ID:59830/79026804310
                -------------------------------------------------------------------""")
            elif showtime.movie.title == "FORREST GUMP":
                print(f"""Booking successful for FORREST GUMP
                -------------------------------------------------------------------
                FORREST GUMP
                U/A English 2D
                TPV Multiplex 3D 4k Dolby Atmos
                ----------------SCAN QR CODE AT CINEMA----------------
                Screen 2,12:00 PM
                Seat Number:{seat_number}
                Booking Date and Time:{x}
                Booking Code:JKSETIND
                Booking ID:05239/38984592634
                -------------------------------------------------------------------""")
            
            elif showtime.movie.title== "THE SHAWSHANK REDEMPTION":
                print(f"""Booking successful for THE SHAWSHANK REDEMPTION
                -------------------------------------------------------------------           
                THE SHAWSHANK REDEMPTION                                                                         
                U/A English 2D                                                                        
                TPV Multiplex 3D 4k Dolby Atmos                                          
                ----------------SCAN QR CODE AT CINEMA----------------           
                Screen 2,10:30 PM                                                               
                Seat Number:{seat_number}
                Booking Date and Time:{x}
                Booking Code:QUGCMNER
                Booking ID:82509/62975613064
                -------------------------------------------------------------------""")
                
            elif showtime.movie.title== "THE GREEN MILE":
                print(f"""Booking successful for THE GREEN MILE
                -------------------------------------------------------------------           
                THE GREEN MILE                                                                          
                U/A English 2D                                                                        
                TPV Multiplex 3D 4k Dolby Atmos                                          
                ----------------SCAN QR CODE AT CINEMA----------------           
                Screen 2,06:30 PM                                                               
                Seat Number:{seat_number}
                Booking Date and Time:{x}
                Booking Code:JSLSVEOF
                Booking ID:90375/28905380583
                -------------------------------------------------------------------""")
            elif showtime.movie.title== "TITANIC":
                print(f"""Booking successful for TITANIC
                -------------------------------------------------------------------           
                TITANIC                                                                          
                U/A ENGLISH 2D                                                                        
                TPV Multiplex 3D 4k Dolby Atmos                                          
                ----------------SCAN QR CODE AT CINEMA----------------           
                Screen 1 Dolby Atmos,08:00 AM                                                               
                Seat Number:{seat_number}
                Booking Date and Time:{x}
                Booking Code:WILKSBFK
                Booking ID:92047/11967284672
                -------------------------------------------------------------------""")
            
        else:
            print("Seat already booked.")

def main():
    system = BookingSystem()

    movie1 = Movie("FORREST GUMP", 192)
    movie2 = Movie("THE PURSUIT OF HAPPYNESS", 195)
    movie3 = Movie("THE SHAWSHANK REDEMPTION", 175)
    movie4 = Movie("THE GREEN MILE", 197)
    movie5 = Movie("TITANIC", 201)
    system.add_movie(movie1)
    system.add_movie(movie2)
    system.add_movie(movie3)
    system.add_movie(movie4)
    system.add_movie(movie5)

    showtime1 = Showtime(movie1, "12:00 PM")
    showtime2 = Showtime(movie2, "03:00 PM")
    showtime3 = Showtime(movie3, "10:30 PM")
    showtime4 = Showtime(movie4, "06:30 PM")
    showtime5 = Showtime(movie5, "08:00 AM")
    system.add_showtime(showtime1)
    system.add_showtime(showtime2)
    system.add_showtime(showtime3)
    system.add_showtime(showtime4)
    system.add_showtime(showtime5)

    while True:
        print("\n1. Display Movies")
        print("2. Display Showtimes")
        print("3. Book Ticket")
        print("4. Exit")

        choice = int(input("Choose an option: "))
        if choice == 1:
            system.display_movies()
        elif choice == 2:
            system.display_showtimes()
        elif choice == 3:
            system.display_showtimes()
            showtime_index = int(input("Choose a showtime: ")) - 1
            seat_number = int(input("Choose a seat number (0-49): "))
            system.book_ticket(showtime_index, seat_number)
        elif choice == 4:
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


                                                                                        
