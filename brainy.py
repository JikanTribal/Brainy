class Interpreter:
    def __init__(self) -> None:
        self.cells = [0]*30000

        self.index = 0
        self.cell_index = 0
        self.stack = []
    
    def exec(self, code: str) -> None:

        while self.index < len(self.code):
            self.char = code[self.index]

            if self.char == "#":
                while self.index < len(self.code):
                    self.char = code[self.index]
                    
                    if ord(self.char) == 10:
                       break
                    self.index += 1
            
            #movimento entre as células (para frenter e para atrás)

            elif self.char == ">":
                if self.cell_index < 30000:
                   self.cell_index += 1
                
                else:
                    self.cell_index == 0

            
            elif self.char == "<":
                if self.cell_index > 0:
                    self.cell_index -= 1
                
                else:
                    self.cell_index = 29999

            #incrementação e decrementação das células

            elif self.char == "+":
                if self.cells[self.cell_index] < 256:
                   self.cells[self.cell_index] += 1
                
                else:
                   self.cells[self.cell_index] = 0
            
            elif self.char == "-":
                if self.cells[self.cell_index] > 0:
                    self.cells[self.cell_index] -= 1
                
                else:
                    self.cells[self.cell_index] = 256
            
            #Entrada e saída

            elif self.char == ",":
                self.cells[self.cell_index] = ord(input()[0])
            
            elif self.char == ".":
                print(chr(self.cells[self.cell_index]), end="")

            elif self.char == "@":
                print(self.cells[self.cell_index])

            #loop
            
            elif self.char == "[":
                if self.cells[self.cell_index] != 0:
                   self.stack.append(self.index)
                
                else:
                    while self.char != "]":
                        self.index += 1
            
            elif self.char == "]":
                if self.cells[self.cell_index] != 0:
                   self.index = self.stack[-1]
                
                else:
                   self.stack.pop()

            self.index += 1
