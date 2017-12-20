"""

@author: eden_juscelino
"""

class Print:
    def __int__(self):
        return  None

    def print_birds(self):
        with open('animals.txt', 'r') as inF:
            number_of_lines = 0
            line_check = 0
            text_file = open("Birds.txt", "w")

            for line in inF:
                book = [line]
                for Bird in book:
                    if "Bird" in Bird:
                        number_of_lines = number_of_lines +1
                        while line_check <number_of_lines:
                            number_of_lines -= 1
                            text_file.write(Bird)
            text_file.close()


    def print_reptiles(self):
        with open('animals.txt', 'r') as inF:
            number_of_lines = 0
            line_check = 0
            text_file = open("Reptiles.txt", "w")

            for line in inF:
                book = [line]
                for Reptile in book:
                    if "Reptile" in Reptile:
                        number_of_lines = number_of_lines +1
                        while line_check <number_of_lines:
                            number_of_lines -= 1
                            text_file.write(Reptile)
            text_file.close()


    def print_mammals(self):
        with open('animals.txt', 'r') as inF:
            number_of_lines = 0
            line_check = 0
            text_file = open("Mammals.txt", "w")

            for line in inF:
                book = [line]
                for Mammal in book:
                    if "Mammal" in Mammal:
                        number_of_lines = number_of_lines +1
                        while line_check <number_of_lines:
                            number_of_lines -= 1
                            text_file.write(Mammal)
            text_file.close()

    def print_aquatics(self):
        with open('animals.txt', 'r') as inF:
            number_of_lines = 0
            line_check = 0
            text_file = open("Aquatics.txt", "w")

            for line in inF:
                book = [line]
                for Aquatic in book:
                    if "Aquatic" in Aquatic:
                        number_of_lines = number_of_lines +1
                        while line_check <number_of_lines:
                            number_of_lines -= 1
                            text_file.write(Aquatic)
            text_file.close()

    def print_insects(self):
        with open('animals.txt', 'r') as inF:
            number_of_lines = 0
            line_check = 0
            text_file = open("Insects.txt", "w")

            for line in inF:
                book = [line]
                for Insect in book:
                    if "Insect" in Insect:
                        number_of_lines = number_of_lines +1
                        while line_check <number_of_lines:
                            number_of_lines -= 1
                            text_file.write(Insect)
            text_file.close()
