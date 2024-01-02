from piece import Piece


class Cube:

     def __init__(self, cube) -> None:
          self.pieces = []
          axis = "kkkkkkkkkjjjjjjjjjiiiiiiiiikkkkkkkkkjjjjjjjjjiiiiiiiii"
          for k in range(3):
               threeby = []
               for i in range(3):
                    row = []
                    for j in range(3):
                         # print(k*9 + j*3 + i)
                         row.append(Piece())
                    threeby.append(row)
               self.pieces.append(threeby)

          k = self.selectFace("k", 1)
          k = self.setSide(k, cube[0:9], "k", 1)
          # self.setFace(k, "k", 1)

          j = self.selectFace("j", 1)
          j = self.setSide(j, cube[9:18], "j", 1)
          # self.setFace(j, "j", 1)

          i = self.selectFace("i", 1)
          i = self.setSide(i, cube[18:27], "i", 1)
          # self.setFace(i, "i", 1)

          k = self.selectFace("k", -1)
          k = self.setSide(k, cube[27:36], "k", -1)
          # self.setFace(k, "k", -1)

          j = self.selectFace("j", -1)
          j = self.setSide(j, cube[36:45], "j", -1)
          # self.setFace(j, "j", -1)

          i = self.selectFace("i", -1)
          i = self.setSide(i, cube[45:54], "i", -1)
          # self.setFace(i, "i", -1)


     def selectFace(self, axis, direction):
          side = []
          if axis == "k":
               if direction == 1:
                    for i in range(3):
                         row = []
                         for j in range(3):
                              row.append(self.pieces[2][j][i])
                         side.append(row)
               else:
                    for i in range(2, -1, -1):
                         row = []
                         for j in range(3):
                              row.append(self.pieces[0][j][i])
                         side.append(row)

          elif axis == "j":
               if direction == 1:
                    for k in range(2, -1, -1):
                         row = []
                         for i in range(2, -1, -1):
                              row.append(self.pieces[k][2][i])
                         side.append(row)
               else:
                    for k in range(2, -1, -1):
                         row = []
                         for i in range(3):
                              row.append(self.pieces[k][0][i])
                         side.append(row)


          elif axis == "i":
               if direction == 1:
                    for k in range(2, -1, -1):
                         row = []
                         for j in range(3):
                              row.append(self.pieces[k][j][2])
                         side.append(row)
               else:
                    for k in range(2, -1, -1):
                         row = []
                         for j in range(2, -1, -1):
                              row.append(self.pieces[k][j][0])
                         side.append(row)

          else:
               print("Error selectFace")
          return side


     def setSide(self, face, sides, axis, direction):
          for j in range(3):
               for i in range(3):
                    face[j][i].addSide(sides[j * 3 + i], axis, direction)
          return face


     def setFace(self, face, axis, direction):
          if axis == "k":
               if direction == 1:
                    for i in range(3):
                         for j in range(3):
                              self.pieces[2][j][i] = face[i][j]
               else:
                    for i in range(2, -1, -1):
                         for j in range(3):
                              self.pieces[0][j][i] = face[2-i][j]

          elif axis == "j":
               if direction == 1:
                    for k in range(2, -1, -1):
                         for i in range(2, -1, -1):
                              self.pieces[k][2][i] = face[2-k][2-i]
               else:
                    for k in range(2, -1, -1):
                         for i in range(3):
                              self.pieces[k][0][i] = face[2-k][i]


          elif axis == "i":
               if direction == 1:
                    for k in range(2, -1, -1):
                         for j in range(3):
                              self.pieces[k][j][2] = face[2-k][j]
               else:
                    for k in range(2, -1, -1):
                         for j in range(2, -1, -1):
                              self.pieces[k][j][0] = face[2-k][2-j]


     def rotateFace(self, axis, direction, clockwise):
          
          face = self.selectFace(axis, direction)
          rotatedFace = []

          if (clockwise and direction == 1) or (not clockwise and direction == -1 ):
               for i in range(3 ):
                    row = []
                    # column.append([face[0][i], face[1][i], face[2][i]])
                    for j in range(2, -1, -1):
                         face[j][i].rotate(axis, clockwise)
                         row.append(face[j][i])
                         
                    rotatedFace.append(row)
          else:
               for i in range(2, -1, -1 ):
                    row = []
                    # column.append([face[0][i], face[1][i], face[2][i]])
                    for j in range(3):
                         # print(face[i][j].matrix)
                         face[j][i].rotate(axis, clockwise)
                         row.append(face[j][i])

                    rotatedFace.append(row)
                
          self.setFace(rotatedFace, axis, direction)

     def move(self, moves):
          for move in moves:
               if move == "u":
                    self.rotateFace("k", 1, True)
               elif move == "U":
                    self.rotateFace("k", 1, False)
               elif move == "r":
                    self.rotateFace("j", 1, True)
               elif move == "R":
                    self.rotateFace("j", 1, False)
               elif move == "f":
                    self.rotateFace("i", 1, True)
               elif move == "F":
                    self.rotateFace("i", 1, False)
               elif move == "d":
                    self.rotateFace("k", -1, True)
               elif move == "D":
                    self.rotateFace("k", -1, False)
               elif move == "l":
                    self.rotateFace("j", -1, True)
               elif move == "L":
                    self.rotateFace("j", -1, False)
               elif move == "b":
                    self.rotateFace("i", -1, True)
               elif move == "B":
                    self.rotateFace("i", -1, False)
               
     def stringRepresentation(self) -> str:
          string = ""

          u = self.selectFace("k", 1)
          for row in u:
               for entry in row:
                    string += str(entry.selectSide("k"))[-1]

          r = self.selectFace("j", 1)
          for row in r:
               for entry in row:
                    string += str(entry.selectSide("j"))[-1]

          f = self.selectFace("i", 1)
          for row in f:
               for entry in row:
                    string += str(entry.selectSide("i"))[-1]

          d = self.selectFace("k", -1)
          for row in d:
               for entry in row:
                    string += str(entry.selectSide("k"))[-1]

          l = self.selectFace("j", -1)
          for row in l:
               for entry in row:
                    string += str(entry.selectSide("j"))[-1]

          b = self.selectFace("i", -1)
          for row in b:
               for entry in row:
                    string += str(entry.selectSide("i"))[-1]
          return string

     def __str__(self) -> str:
          string = ""
          i = 0
          sides = self.stringRepresentation()
          # print(sides)
          u = sides[0:9]
          for j in range(3):
               string += "        "
               for i in range(3):
                    string += u[j * 3 + i] + " "
               string += "\n"

          l = sides[36:45]
          f = sides[18:27]
          r = sides[9:18]
          b = sides[45:54]

          for j in range(3):
               string += " "
               for i in range(3):
                    string += l[j * 3 + i] + " "

               string += " "
               for i in range(3):
                    string += f[j * 3 + i] + " "

               string += " "
               for i in range(3):
                    string += r[j * 3 + i] + " "

               string += " "
               for i in range(3):
                    string += b[j * 3 + i] + " "

               string += "\n"

          d = sides[27:36]
          for j in range(3):
               string += "        "
               for i in range(3):
                    string += d[j * 3 + i] + " "
               string += "\n"

          return string
# cube = Cube("wwwwwwwwwrrrrrrrrrgggggggggyyyyyyyyyooooooooobbbbbbbbb")
# cube = Cube("123456789123rrrrrr456ggggggyyyyyyyyyooooooooobbbbbbbbb")
# cube = Cube("123456789123456789123456789123456789123456789123456789")
cube = Cube("wwrwwyooygrbrrbywywgryggbrbwbroyogoorrggogoyowbgybwbby")

"rufubdlrfbdurrlfb"
print(cube)
cube.move("BFLRRUDBFRLDBUFUR")
print(cube)
# print("\nkp")
# cube.rotateFace("k", -1, True)
# print(cube)
# cube.rotateFace("k", -1, False)
# print(cube)

# print("\nj")
# cube.rotateFace("j", 1, True)
# print(cube)
# cube.rotateFace("j", 1, False)
# print(cube)

# print("\njp")
# cube.rotateFace("j", -1, True)
# print(cube)
# cube.rotateFace("j", -1, False)
# print(cube)

# print("\ni")
# cube.rotateFace("i", 1, True)
# print(cube)
# cube.rotateFace("i", 1, False)
# print(cube) 

# print("\nip")
# cube.rotateFace("i", -1, True)
# print(cube)
# cube.rotateFace("i", -1, False)
# print(cube)

# for k in range(3):
#      for j in range(3):
#           for i in range(3):
#                print(k,j,i)
#                print(cube.pieces[k][j][i])

