"""

@author: eden_juscelino
"""


class Catalog:
    def __int__(self):
        return None

    def getImage(self):

        from graphics import GraphicsWindow
        win = GraphicsWindow(800, 800)
        canvas = win.canvas()
        canvas.drawRect(20, 30, 760, 0)

        with open('animals.txt', 'r') as inF:
            canvas.drawText(310, 50, "Korea Zootopia Animals Catalog")
            canvas.drawRect(20, 80, 760, 0)
            canvas.drawText(50,100, "Aquatics")
            conta =120
            counter = 1

            number_of_lines = 0
            line_check = 0
            for line in inF:
                book = [line]

                for lines in book:

                    if "Aquatic" in lines:

                        number_of_lines = number_of_lines +1

                        while line_check <number_of_lines:
                            number_of_lines = number_of_lines -1
                            eu =str(lines)
                            a1,a2,a3 =eu.split(" ")
                            canvas.drawText(30,conta, counter)
                            canvas.drawText(50,conta, a1)
                            canvas.drawText(130,conta, a2)
                            counter += 1
                            conta = conta + 20






        with open('animals.txt', 'r') as inF:

            canvas.drawRect(20, conta, 760, 0)
            canvas.drawText(50,conta+20, "Mammals")
            conta =conta +40
            counter = 1

            number_of_lines = 0
            line_check = 0
            for line in inF:
                book = [line]

                for lines in book:

                    if "Mammal" in lines:

                        number_of_lines = number_of_lines +1

                        while line_check <number_of_lines:
                            number_of_lines = number_of_lines -1
                            eu =str(lines)
                            a1,a2,a3 =eu.split(" ")
                            canvas.drawText(30,conta, counter)
                            canvas.drawText(50,conta, a1)
                            canvas.drawText(130,conta, a2)
                            counter += 1
                            conta = conta + 20





        with open('animals.txt', 'r') as inF:

            canvas.drawRect(20, conta, 760, 0)
            canvas.drawText(50,conta+20, "Birds")
            conta =conta +40
            counter = 1

            number_of_lines = 0
            line_check = 0
            for line in inF:
                book = [line]

                for lines in book:

                    if "Bird" in lines:

                        number_of_lines = number_of_lines +1

                        while line_check <number_of_lines:
                            number_of_lines = number_of_lines -1
                            eu =str(lines)
                            a1,a2,a3 =eu.split(" ")
                            canvas.drawText(30,conta, counter)
                            canvas.drawText(50,conta, a1)
                            canvas.drawText(130,conta, a2)
                            counter += 1
                            conta = conta + 20



        with open('animals.txt', 'r') as inF:

            canvas.drawRect(20, conta, 760, 0)
            canvas.drawText(50,conta+20, "Reptiles")
            conta =conta +40
            counter = 1

            number_of_lines = 0
            line_check = 0
            for line in inF:
                book = [line]

                for lines in book:

                    if "Reptile" in lines:

                        number_of_lines = number_of_lines +1

                        while line_check <number_of_lines:
                            number_of_lines = number_of_lines -1
                            eu =str(lines)
                            a1,a2,a3 =eu.split(" ")
                            canvas.drawText(30,conta, counter)
                            canvas.drawText(50,conta, a1)
                            canvas.drawText(130,conta, a2)
                            counter += 1
                            conta = conta + 20

        with open('animals.txt', 'r') as inF:

            canvas.drawRect(20, conta, 760, 0)
            canvas.drawText(50,conta+20, "Insects")
            conta =conta +40
            counter = 1

            number_of_lines = 0
            line_check = 0
            for line in inF:
                book = [line]

                for lines in book:

                    if "Insect" in lines:

                        number_of_lines = number_of_lines +1

                        while line_check <number_of_lines:
                            number_of_lines = number_of_lines -1
                            eu =str(lines)
                            a1,a2,a3 =eu.split(" ")
                            canvas.drawText(30,conta, counter)
                            canvas.drawText(50,conta, a1)
                            canvas.drawText(130,conta, a2)
                            counter += 1
                            conta = conta + 20





        win.wait()
