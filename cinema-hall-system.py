

class Star_cinema:
    __hall_list=[]

    def entry_hall(self,hall):
        Star_cinema.__hall_list.append(hall)

  


class Hall(Star_cinema):
    __hall_no_start=100
    
    def __init__(self,rows,cols) -> None:
        self.__seats={}
        self.__show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=Hall.__hall_no_start
        Hall.__hall_no_start+=1
        self.entry_hall(self)
    
    
    def entry_show(self,id,movie_name,time):
        self.__show_list.append((id,movie_name,time))
        self.__seats[id] = [[0 for i in range(self.__cols)] for j in range(self.__rows)]
    

    def __validate_position(self,row,col):
        if 0<= row < self.__rows and 0 <= col < self.__cols:
            return True
        else:
            return False

    def __is_occupied(self,seat_maze,row,col):
        if seat_maze[row][col] == 1:
            return True
        else: 
            return False
    def validate_show_id(self,show_id):
         if self.__seats.get(show_id)==None:
             return False
         else :
             return True


    def book_seats(self,show_id, seat_list):
        if  self.validate_show_id(show_id) is False:
            print("Invalid id: No show is running with that id!")
            return
        
        seat_maze= self.__seats[show_id]

        for row,col in seat_list:
            row-=1
            col-=1
            if not self.__validate_position(row,col):
                print(f'This seat is invalid: ({row+1}, {col+1})')
            elif self.__is_occupied(seat_maze,row,col) is True: 
                print(f'This seat is occupied: ({row+1}, {col+1})')
            else:
                self.__seats[show_id][row][col]=1
                print(f'Seat ({row+1}, {col+1}) booked for show {show_id}')
     

    def view_show_list(self):
        if len(self.__show_list) == 0:
            print('No shows are currently running!')
        for (id,movie_name,time) in self.__show_list:
            print(f'MOVIE NAME: {movie_name}({id}) Show Id: {id} Time: {time}')
     
    def view_available_seats(self,show_id):
        if  self.validate_show_id(show_id) is False :
            print("Invalid id: No show is running with that id!")
            return
        
        print(f'\nAvailable seats for show: {show_id}\n')

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[show_id][i][j]==0:
                    print(f'({i+1}, {j+1})')

        print('\nAvailable seats in matrix format: \n')
        for row in self.__seats[show_id]:
            print(row) 




def run():
        options ="""
                    1. VIEW ALL SHOW TODAY
                    2. VIEW AVAILABLE SEATS
                    3. BOOK TICKET
                    4. EXIT
Enter Option:"""
        while True:
            key= int(input(options))
            if key== 1:
                hall_1.view_show_list()
            elif key ==2:
                inp=int(input('Please enter show id: '))
                hall_1.view_available_seats(inp)
            elif key==3:
                inp=int(input('Please enter show id: '))
                if hall_1.validate_show_id(inp) is False:
                    print("Invalid id: No show is running with that id!")
                    continue
                
                tic_count=int(input('Please enter the number of tickets: '))
                aux=[]
                for i in range(1,tic_count+1):
                    row= int(input(f'Please enter seat Row for ticket: {i}: '))
                    col= int(input(f'Please enter seat Col for ticket: {i}: '))
                    aux.append((row,col))

                hall_1.book_seats(inp,aux)
            elif key==4:
                break
            else: print('Please enter a valid key!')


# Create Hall instances
hall_1=Hall(4,4)

# Hall 1 shows
hall_1.entry_show(3001,'spiderman','2pm')
hall_1.entry_show(2040,'Avengers End game','6am')
hall_1.entry_show(5102,'batman','10pm')


run()