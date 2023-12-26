from piece import Piece

class Cube():
    
    
     def selectFace(self,axis, direction):
          side = []
          if axis == "k":
               for j in range(3):
                    row = []
                    for i in range(3):
                         row.append(self.pieces[1 - direction][j][i])
                    side.append(row)
          elif axis == "j":
               for k in range(3):
                    row = []
                    for i in range(3):
                         row.append(self.pieces[k][1 - direction][i])
                    side.append(row)

          elif axis == "i":
               for k in range(3):
                    row = []
                    for j in range(3):
                         row.append(self.pieces[k][j][1 - direction])
                    side.append(row)

          else:
               print("Error selectFace")
          return side

     def setSide(self, face, sides, axis, direction):
          for j in range(3):
               for i in range(3):
                    face[j][i].addSide(sides[j*3 + i], axis, direction)
          return face
     
     def setFace(self, face, axis, direction):
          if axis == "k":
               for j in range(3):
                    for i in range(3):
                         self.pieces[1 - direction][j][i] = face[j][i]
                    
          elif axis == "j":
               for k in range(3):
                    for i in range(3):
                         self.pieces[k][1-direction][i] = face[k][i]
                    

          elif axis == "i":
               for k in range(3):
                    for j in range(3):
                         self.pieces[k][j][1-direction] = face[k][j]

     def rotateFace(self, face, clockwise):
          # print(face)
          rotatedFace = []
          for i in range(3):
               row = []
               for j in range(3):
                    # face[j][i].rotate("k", True)
                    row.append(face[j][i])
               rotatedFace.append(row)
          # print(rotatedFace)
          return rotatedFace
 
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
          self.setFace(k, "k", 1)

          j = self.selectFace("j", 1)
          j = self.setSide(j, cube[9:18], "j", 1)
          self.setFace(j, "j", 1)

          i = self.selectFace("i", 1)
          i = self.setSide(i, cube[18:27], "i", 1)
          self.setFace(i, "i", 1)

          k = self.selectFace("k", -1)
          k = self.setSide(k, cube[27:36], "k", -1)
          self.setFace(k, "k", -1)

          j = self.selectFace("j", -1)
          j = self.setSide(j, cube[36:45], "j", -1)
          self.setFace(j, "j", -1)

          i = self.selectFace("i", -1)
          i = self.setSide(i, cube[45:54], "i", -1)
          self.setFace(i, "i", -1)


          piece = self.pieces[0][0][0]
          print(piece.matrix)


          f = self.selectFace("k", 1)
          f = self.rotateFace(f, True)
          self.setFace(f, "k", 1)


          piece = self.pieces[0][0][0]
          print(piece.matrix)
          

          # k_ = self.selectFace("k", 1)
          # for i in range(3):
          #      for j in range(3):
          #           print(k_[i][j].matrix)
          # z = 0
          # for t, direction in enumerate([1, -1], start= 1):
          #      print(direction, z)      
               
          #      for j in range(3):
          #           for i in range(3):
          #                pieces[k][j][i].addSide(cube[z], axis[z], direction)
          #                print(pieces[k][j][i].matrix)
          #                z += 1
                    
          # for matrix in self.pieces:
          #      for row in matrix:
          #           for piece in row:
          #                print(piece.matrix)
          # print(pieces[0][0][1].matrix)
          # pieces[1][1][1].rotate("k", True)
          # print(pieces[1][1][1].matrix)
          # pieces[1][1][1].rotate("k", False)
          # print(pieces[1][1][1].matrix)

          
                

cube = Cube("wwwwwwwwwrrrrrrrrrgggggggggyyyyyyyyyooooooooobbbbbbbbb")
