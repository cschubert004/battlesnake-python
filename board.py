import os


test_data = {
    "board": {
        "food": [
            {
                "x": 6,
                "y": 10
            },
            {
                "x": 5,
                "y": 5
            }
        ],
        "hazards": [],
        "height": 11,
        "snakes": [
            {
                "body": [
                    {
                        "x": 5,
                        "y": 9
                    },
                    {
                        "x": 5,
                        "y": 9
                    },
                    {
                        "x": 5,
                        "y": 9
                    }
                ],
                "head": {
                    "x": 5,
                    "y": 9
                },
                "health": 100,
                "id": "gs_QSCrCBB8XtGYxh7qSJWKxVrX",
                "latency": "",
                "length": 3,
                "name": "cs_test_snake",
                "shout": ""
            }
        ],
        "width": 11
    },
    "game": {
        "id": "91e7bd2b-7a3e-40de-89af-69adfb94a572",
        "ruleset": {
            "name": "solo",
            "version": "v1.0.17"
        },
        "timeout": 500
    },
    "turn": 0,
    "you": {
        "body": [
            {
                "x": 5,
                "y": 9
            },
            {
                "x": 5,
                "y": 9
            },
            {
                "x": 5,
                "y": 9
            }
        ],
        "head": {
            "x": 5,
            "y": 9
        },
        "health": 100,
        "id": "gs_QSCrCBB8XtGYxh7qSJWKxVrX",
        "latency": "",
        "length": 3,
        "name": "cs_test_snake",
        "shout": ""
    }
}


class point:
    def __init__(self):
        self.is_food = False
        self.is_snake = False
        self.is_tail = False
        self.is_head = False
        self.is_me = False
        self.value = 0.5


class board:
    
    #def __init__(self, width, height):
    #    self.width = width
    #    self.height = height
    #    self.map_data = self.create_board(width, height)

    def __init__(self, data):
        self.width = -1
        self.height = -1
        self.map_data = []
        self.parse_board(data)


    def create_board(self, width, height):
        board  = []
        for col in range(width):
            colarray = []
            for row in range(height):
                map_point = point()
                colarray.append(map_point)
            
            board.append(colarray)
        return board

    
    def parse_board(self,data):
        self.width = data['width']
        self.height = data['height']
        # create a blank board
        self.map_data = self.create_board(self.width, self.height)

        # add the food
        for piece in data['food']:
            self.map_data[piece['x']][piece['y']].is_food = True

        
        for snake in data['snakes']:
            for segment in snake['body']:
                self.map_data[segment['x']][segment['y']].is_snake = True


    def print_board(self):
        # bottom left corner is 0,0, so start from top of height
        for row in reversed(range (self.height)):
            print ('[ {:<2} ]'.format(row), end='')
            for col in range (self.width):
                stringval = self.get_point_string(self.map_data[col][row])
                print('|{:<4}'.format(stringval),end='')
            print('')

        print ('[ {:<2} ]'.format(' '), end='')

        for col in range (self.width):
            print ('[ {:<2}]'.format(col), end='')
        print('')


    def get_point_string(self, point):
        if point.is_snake:
            return 's'
        elif point.is_food:
            return 'f'
        else:
            return str(point.value)


    def check_coords(self, x, y):
        if x < self.width and y < self.height and x >= 0  and y >= 0:
            return True
        else:
            return False

    def set_val (self, x, y, value):
        if self.check_coords(x,y):
            self.map_data[x][y] = value
        else:
            raise ("Out of bounds")

    def get_val (self, x, y):
        if self.check_coords(x,y):
            return self.map_data[x][y]
        else:
            raise ("Out of bounds")

    
    def is_valid_coordinate(self,x,y):
        # check if it's off the board
        if self.check_coords(x, y) == False:
            return False
        else:
            # valid coord - check if anything is there
            map_point = self.map_data[x][y]
            if map_point.is_snake:
                return False
            else:
                return True
    
    def get_allowable_moves(self, x,y):
        possible_moves = ["up", "down", "left", "right"]

        print ("checking {},{}".format(x,y))
        # check point above
        if not self.is_valid_coordinate(x, y+1):
            possible_moves.remove("up")

        # check point below
        if not self.is_valid_coordinate(x, y-1):
            possible_moves.remove("down")

        # check point to left
        if not self.is_valid_coordinate(x-1, y):
            possible_moves.remove("left")
        
        # check point ot right
        if not self.is_valid_coordinate(x+1, y):
            possible_moves.remove("right")

        return possible_moves



board = board(test_data['board'])
board.print_board()
print (board.get_allowable_moves(test_data['you']['head']['x'], test_data['you']['head']['y']))
print (board.get_allowable_moves(5,10))
print (board.get_allowable_moves(0,0))
print (board.get_allowable_moves(10,10))
print (board.get_allowable_moves(10,0))
print (board.get_allowable_moves(0,10))
print (board.get_allowable_moves(4,9))
