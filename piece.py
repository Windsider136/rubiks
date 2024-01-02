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


class Piece:
    def __init__(self) -> None:
        self.matrix = []  # Column vectors

    def addSide(self, colour, axis, direction):
        if axis == "k":
            self.matrix.append([0, 0, Colour(colour, direction)])
        elif axis == "j":
            self.matrix.append([0, Colour(colour, direction), 0])
        elif axis == "i":
            self.matrix.append([Colour(colour, direction), 0, 0])

        else:
            print("error")
        # print(self.matrix)

    def rotate(self, axis, clockwise):
        new_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        # Rotation matrices (column wise)
        kcw = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]  
        kccw = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
        jcw = [[0,0,1], [0,1,0], [-1,0,0]]
        jccw = [[0,0,-1], [0,1,0], [1,0,0]]
        iccw = [[1,0,0], [0,0,-1], [0,1,0]]
        icw = [[1,0,0], [0,0,1], [0,-1,0]]

        def matrixMult(self, matrix):
            for i in range(len(self.matrix)):
                    for j in range(3):
                        new_matrix[i][j] = (
                            self.matrix[i][0] * matrix[j][0]
                            + self.matrix[i][1] * matrix[j][1]
                            + self.matrix[i][2] * matrix[j][2]
                        )
            self.matrix = new_matrix


        if axis == "k":
            if clockwise:
                matrixMult(self, kcw)
            else:
                matrixMult(self, kccw)
        elif axis == "j":
            if clockwise:
                matrixMult(self, jcw)
            else:
                matrixMult(self, jccw)
        elif axis == "i":
            if clockwise:
                matrixMult(self, icw)
            else:
                matrixMult(self, iccw)
        else:
            raise ValueError

        # if axis == "k":
        #     if clockwise:
        #         for i in range(len(self.matrix)):
        #             for j in range(3):
        #                 new_matrix[i][j] = (
        #                     self.matrix[i][0] * kcw[j][0]
        #                     + self.matrix[i][1] * kcw[j][1]
        #                     + self.matrix[i][2] * kcw[j][2]
        #                 )
            
        #     else:
        #         for i in range(len(self.matrix)):
        #             for j in range(3):
        #                 new_matrix[i][j] = (
        #                     self.matrix[i][0] * kccw[j][0]
        #                     + self.matrix[i][1] * kccw[j][1]
        #                     + self.matrix[i][2] * kccw[j][2]
        #                 )
    


        # self.matrix = new_matrix

    def selectSide(self, axis):
        side = 0
        if axis == "k":
            for column in self.matrix:
                side += column[2] * 1
        elif axis == "j":
            for column in self.matrix:
                side += column[1] * 1
        elif axis == "i":
            for column in self.matrix:
                side += column[0] * 1
        else:
            raise ValueError

        return side
    
    def getSide(self, axis):
        testValue = 0
        if axis == "k":
            for i in range(len(self.matrix)):
                testValue += self.matrix[i][2] * 1
        elif axis == "j":
            for i in range(len(self.matrix)):
                testValue += self.matrix[i][1] * 1
        else:
            for i in range(len(self.matrix)):
                testValue += self.matrix[i][0] * 1
        return testValue

    def __str__(self) -> str:
        string = ""
        for i in range(3):
            for j in range(len(self.matrix)):
                string += str(self.matrix[j][i]) + " "
            string += "\n"
        return string


# """Test centre piece"""

# piece = Piece()

# piece.addSide("w", "k", 1)

# # Test 1
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][2] * 1

# if testValue.colour != "w":
#     print("Error test 1")

# # Test 2    
# piece.rotate("k", True)

# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][2] * 1

# if testValue.colour != "w":
#     print("Error test 2")

# # Test 3
# piece.rotate("k", True)
# piece.rotate("k", True)

# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][2] * 1

# if testValue.colour != "w":
#     print("Error test 3")


# """Test corner piece"""

# piece = Piece()

# piece.addSide("w", "k", 1)
# piece.addSide("o", "j", -1)
# piece.addSide("g", "i", 1)

# piece.rotate("k", True)
# piece.rotate("k", False)

# # Test 4
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][0] * 1

# if testValue.colour != "g" or testValue.value != 1:
#     print("Error test 4")

# # Test 5
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][1] * 1

# if testValue.colour != "o" or testValue.value != -1:
#     print("Error test 5")

# # Test 6
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][2] * 1

# if testValue.colour != "w" or testValue.value != 1:
#     print("Error test 6")

# piece.rotate("k", True)

# # Test 7
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][0] * 1

# if testValue.colour != "o" or testValue.value != -1:
#     print("Error test 7")

# # Test 8
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][1] * 1

# if testValue.colour != "g" or testValue.value != -1:
#     print("Error test 8")

# # Test 9
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][2] * 1

# if testValue.colour != "w" or testValue.value != 1:
#     print("Error test 9")

# piece.rotate("k", False)
# piece.rotate("j", True)
# piece.rotate("j", False)
# piece.rotate("i", True)
# piece.rotate("i", False)


# # Test 10
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][0] * 1

# if testValue.colour != "g" or testValue.value != 1:
#     print("Error test 10")

# # Test 11
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][1] * 1

# if testValue.colour != "o" or testValue.value != -1:
#     print("Error test 11")

# # Test 12
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][2] * 1

# if testValue.colour != "w" or testValue.value != 1:
#     print("Error test 12")


# piece.rotate("j", True)
# # Test 13
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][0] * 1

# if testValue.colour != "w" or testValue.value != 1:
#     print("Error test 13")

# # Test 14
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][1] * 1

# if testValue.colour != "o" or testValue.value != -1:
#     print("Error test 14")

# # Test 15
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][2] * 1

# if testValue.colour != "g" or testValue.value != -1:
#     print("Error test 15")

# piece.rotate("j", False)
# piece.rotate("i", True)

# # Test 16
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][0] * 1

# if testValue.colour != "g" or testValue.value != 1:
#     print("Error test 16")

# # Test 17
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][1] * 1

# if testValue.colour != "w" or testValue.value != 1:
#     print("Error test 17")

# # Test 18
# testValue = 0
# for i in range(len(piece.matrix)):
#     testValue += piece.matrix[i][2] * 1

# if testValue.colour != "o" or testValue.value != 1:
#     print("Error test 18")


