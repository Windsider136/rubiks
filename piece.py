from dataclasses import dataclass

@dataclass
class Colour:
    colour: str
    value: int
    def __mul__(self, y):
        
        if self.value * y == 0:
            return 0
        self.value = self.value * y
        return self
    
    def __rmul__(self, y):
        
        if self.value * y == 0:
            return 0
        self.value = self.value * y
        return self
    
    def __add__(self, y):
        self.value += y
        return self
    
    def __radd__(self, y):
        self.value += y

        return self
    
    def __str__(self):
        if self.value > 0:
            return self.colour
        else:
            return "-" + self.colour

class Piece():

    def __init__(self) -> None:
        self.matrix = [] #Row vectors
    
    def addSide(self, colour, axis, direction):
        if axis == "k":
            self.matrix.append([0,0,Colour(colour, direction)])
        elif axis == "j":
            self.matrix.append([0, Colour(colour, direction), 0])
        elif axis == "i":
            self.matrix.append([Colour(colour, direction), 0, 0])
        
        else:
            print("error")    
        # print(self.matrix)

    def rotate(self, axis, clockwise):
        new_matrix = [[0,0,0], [0,0,0], [0,0,0]]
        kcw = [[0,1,0], [-1,0,0], [0,0,1]] #Column vectors
        kccw = [[0,-1,0], [1,0,0], [0,0,1]]
        if axis == 'k':
            if clockwise:
                for i in range(3):
                    for j in range(3):
                        new_matrix[i][j] = self.matrix[i][0] * kcw[j][0] + self.matrix[i][1] * kcw[j][1] + self.matrix[i][2] * kcw[j][2]
            else:
                for i in range(3):
                    for j in range(3):
                        new_matrix[i][j] = self.matrix[i][0] * kccw[j][0] + self.matrix[i][1] * kccw[j][1] + self.matrix[i][2] * kccw[j][2]
                
                
        self.matrix = new_matrix




    def __str__(self) -> str:
        string =""
        for x in self.matrix:
            string += str(x[0]) + " " +  str(x[1])+ " " + str(x[2]) + "\n"
        return string


# red = Colour('r', 1)
# blue = Colour('b', 1)
# white = Colour('w', 1)

# piece = Piece(white, red, blue)

# print(piece)

# piece.rotate("k", False)
# print(piece)
# piece.rotate("k", True)
# print(piece)
# piece.rotate("k", False)
# print(piece)
# piece.rotate("k", True)
# print(piece)

# piece.rotate("k", True)
# print(piece)
# piece.rotate("k", True)
# print(piece)
# piece.rotate("k", False)
# print(piece)
# piece.rotate("k", False)
# print(piece)
