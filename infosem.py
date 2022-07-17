print("Information Semiotics, v1 ")

class sign_relation:
    def __init__(self, string_obect, corres, translatant):
        self.string_obect = string_obect
        self.corres = corres
        self.translatant = translatant

    def printObect(self):
        print(self.string_obect)

#sign1 = sign_relation("9900009", "is next to", "092429")
#sign1.printObect()

#create a data type that captures the intuition of string substitution system
#simply correspond single symbols into one or more symbols different symbols.

class stochastic_sign:
    def __init__(self, meaning, prob):
        self.meaning = meaning
        self.prob = prob


stringsub = {
    "1": "100",
    "0": "111"
}






