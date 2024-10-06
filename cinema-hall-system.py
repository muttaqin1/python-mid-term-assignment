

class Star_cinema:
    __hall_list=[]
    
    def __init__(self) -> None:
        pass

    def entry_hall(self,hall):
        Star_cinema.__hall_list.append(hall)



class Hall(Star_cinema):
    __hall_count=100
    
    def __init__(self,rows,cols) -> None:
        self.__seats={}
        self.__show_list=[]
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=Hall.__hall_count
        Hall.__hall_count+=1
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


    def book_seats(self,show_id, seat_list):
        if self.__seats.get(show_id)==None:
            print("Invalid id: No show is running with that id!")
            return
        
        seat_maze= self.__seats[show_id]

        for row,col in seat_list:
            row-=1
            col-=1
            if self.__validate_position(row,col) is False:
                print(f'This seat is invalid: ({row+1}, {col+1})')
            elif self.__is_occupied(seat_maze,row,col) is True: 
                print(f'This seat is occupied: ({row+1}, {col+1})')
            else:
                self.__seats[show_id][row][col]=1
                print(f'Seat ({row+1}, {col+1}) booked for show {show_id}')
    
    
    def view_show_list(self):
        if len(self.__show_list) == 0:
            print('\nNo shows are currently running!\n')
        for (id,movie_name,time) in self.__show_list:
            print(f'\nMOVIE NAME: {movie_name}({id}) Show Id: {id} Time: {time}\n')
     
    def view_available_seats(self,id):
        print(f'\nAvailable seats for show: {id}\n')

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[id][i][j]==0:
                    print(f'({i+1}, {j+1})')

        print('\nAvailable seats in matrix format: \n')
        for row in self.__seats[id]:
            print(row) 


    def print_state(self):
        print('seats: ',self.__seats)
        print('show_list: ',self.__show_list)
        print('rows: ',self.__rows)
        print('cols: ',self.__cols)
        print('hall_no: ',self.__hall_no)
        print('hall_count: ', Hall.__hall_count)


hall1=Hall(4,4)
hall1.entry_show(10,'spiderman','2pm')
hall1.book_seats(10,[(3,3),(4,4),(2,5),(2,2),(1,1),(3,3)])
# hall1.print_state()
hall1.view_show_list()
hall1.view_available_seats(10)