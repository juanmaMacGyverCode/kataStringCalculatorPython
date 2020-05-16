class StringCalculator:

    def __init__(self):
        pass

    def add(self, text):

        self.errors = ""

        text = self.__treatment_of_custom_separators(text)

        self.__find_errors(text)
        if len(self.errors) > 0:
            return self.errors

        return self.__to_do_add(text)

    def __to_find_negative_numbers(self, text):

        numbersOnList = self.__change_text_with_list(text, "\n")

        negativeNumbers = ""
        for number in numbersOnList:
            try:
                if number != "" and (number[0] == "-" or self.__is_numeric_or_float(number)) and float(number) < 0:
                    raise ValueError("El nombre no está completo")
            except ValueError:
                negativeNumbers += number + ","

        negativeNumbers = negativeNumbers[0:len(negativeNumbers)-1]

        if len(negativeNumbers) > 0:
            self.__phrase_self_error("Negative not allowed : " + negativeNumbers + ".")
        
    def __phrase_self_error(self, error):
        if len(self.errors) > 0:
            self.errors += "\n" + error
        else:
            self.errors += error


    def __treatment_of_custom_separators(self, text):
        haveTwoSlash = text.find("//") == 0
        if haveTwoSlash:
            if text[len(text) - 1] == "\n":
                return "0"

            splitTheCustomExpresion = text.split("\n")
            separator = splitTheCustomExpresion[0][2:]
            phraseWithoutSeparator = splitTheCustomExpresion[1].split(separator)

            import re

            for count in range(0, len(phraseWithoutSeparator)):
                if phraseWithoutSeparator[count] != "" and (self.__is_numeric_or_float(phraseWithoutSeparator[count]) == None or self.__is_numeric_or_float(phraseWithoutSeparator[count]).group() != phraseWithoutSeparator[count]):
                    fragmento = re.search("[0-9]+([.][0-9]+)?", phraseWithoutSeparator[count]).group()
                    if re.search("[0-9]+([.][0-9]+)?", phraseWithoutSeparator[count][0]) == None:
                        fragmentoErroneo = splitTheCustomExpresion[1][splitTheCustomExpresion[1].find(fragmento)-1]
                        self.errors += "'" + separator + "' expected but '" + fragmentoErroneo + "' found at position " + str(splitTheCustomExpresion[1].find(fragmento)-1) + "."
                    else:
                        caracteresAnterioresCorrectos = self.__is_numeric_or_float(phraseWithoutSeparator[count]).group()
                        posicionError = re.search(caracteresAnterioresCorrectos, splitTheCustomExpresion[1]).end()
                        self.errors += "'" + separator + "' expected but '" + splitTheCustomExpresion[1][posicionError] + "' found at position " + str(posicionError) + "."
            text = splitTheCustomExpresion[1].replace(separator, ",")
            return text
        return text

    def __to_do_add(self, text):
        numbers = self.__change_text_with_list(text, "\n")

        if self.__are_there_many_numbers(numbers):
            return self.__addAllNumbers(numbers)
        if self.__is_numeric_or_float(text):
            return text
        else:
            return "0"

    def __find_errors(self, text):

        if len(text) > 0:
            self.__to_find_negative_numbers(text)
        self.__error_number_expected(text)
        self.__error_final_separator(text)

    def __error_final_separator(self, text):
        if len(text) > 1 and (text[len(text) - 1] == "," or text[len(text) - 1] == "\n"):
            self.__phrase_self_error("Number expected but EOF found.")

    def __error_number_expected(self, text):
        mapErrors = {}
        mapErrors = self.__find_patterns(",\n", text, mapErrors)
        mapErrors = self.__find_patterns("\n,", text, mapErrors)
        mapErrors = self.__find_patterns(",,", text, mapErrors)
        mapErrors = self.__find_patterns("\n\n", text, mapErrors)
        
        errorPhrase = ""
        if len(mapErrors) > 0:
            for error in mapErrors:
                self.__phrase_self_error("Number expected but '" + self.__checkIfNewline(mapErrors[error][1]) + "' found at position " + str(error + 1) + ".")

        return errorPhrase

    def __find_patterns(self, pattern, text, mapErrors):
        import re
        for match in re.finditer(pattern, text):
            start = match.start()
            group = match.group()
            mapErrors[start] = group
        return mapErrors


    def __checkIfNewline(self, character):
        if character == "\n":
            return "\\n"
        return character

    def __change_text_with_list(self, text, pattern):
        text = text.replace(pattern, ",")
        return text.split(",")

    def __are_there_many_numbers(self, numbers):
        return len(numbers) > 1

    def __is_numeric_or_float(self, text): 
        import re
        return re.match("[0-9]+[.][0-9]+|[0-9]+", text)

    def __addAllNumbers(self, numbers):
        import functools
        import operator
        return str(functools.reduce(lambda a, b: float(a)+float(b), numbers))

