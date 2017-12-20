"""

@author: eden_juscelino
"""


class Chart:
    def __int__(self):
        return None

    def getChart(self):

        from graphics import GraphicsWindow
        win = GraphicsWindow(800, 400)
        canvas = win.canvas()
        canvas.drawRect(20, 30, 760, 0)

        with open('animals.txt', 'r') as inF:
            canvas.drawText(310, 50, "Korea Zootopia Animals Bar Chart")
            conta =100
            canvas.drawRect(20, 80, 760, 0)
            canvas.drawText(50,conta, "Aquatics")


            number_of_lines = 0

            for line in inF:
                book = [line]

                for lines in book:

                    if "Aquatic" in lines:
                        number_of_lines = number_of_lines +1


        canvas.setColor("blue")
        canvas.drawRect(120, conta, number_of_lines*20, 20)
        conta += 30



        with open('animals.txt', 'r') as inF:

            canvas.setColor("black")
            canvas.drawText(50,conta, "Mammals")



            for line in inF:
                book = [line]

                for lines in book:

                    if "Mammal" in lines:

                        number_of_lines = number_of_lines +1

        canvas.setColor("green")
        canvas.drawRect(120, conta, number_of_lines*20, 20)
        conta += 30


        with open('animals.txt', 'r') as inF:

            canvas.setColor("black")
            canvas.drawText(50,conta, "Birds")

            for line in inF:
                book = [line]

                for lines in book:

                    if "Bird" in lines:

                        number_of_lines = number_of_lines +1

        canvas.setColor("yellow")
        canvas.drawRect(120, conta, number_of_lines*20, 20)
        conta += 30


        with open('animals.txt', 'r') as inF:
            canvas.setColor("black")
            canvas.drawText(50,conta, "Reptiles")
            number_of_lines = 0

            for line in inF:
                book = [line]

                for lines in book:

                    if "Reptile" in lines:

                        number_of_lines = number_of_lines +1

        canvas.setColor("pink")
        canvas.drawRect(120, conta, number_of_lines*20, 20)
        conta += 30
        with open('animals.txt', 'r') as inF:

            canvas.setColor("black")
            canvas.drawText(50,conta, "Insects")
            number_of_lines = 0
            for line in inF:
                book = [line]

                for lines in book:

                    if "Insect" in lines:

                        number_of_lines = number_of_lines +1

        canvas.setColor("purple")
        canvas.drawRect(120, conta, number_of_lines*20, 20)
        conta += 30
        win.wait()
