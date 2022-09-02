#Information Semiotics

class triadic_sign_relation:
    def __init__(self, string_obect, corres, translatant):
        self.string_obect = string_obect
        self.corres = corres
        self.translatant = translatant

    def printObect(self):
        print(self.string_obect)

class dyadic_sign_relation:
    def __init__(self, string_object, corres):
        self.string_object = string_object
        self.corres = corres

    def printObject(self):
        print(self.string_object)

#sign1 = sign_relation("9900009", "is next to", "092429")
#sign1.printObect()

#create a data type that captures the intuition of string substitution system
#simply correspond single symbols into one or more symbols different symbols.

class stochastic_sign:
    def __init__(self, meaning, prob):
        self.meaning = meaning
        self.prob = prob

def semic_density(s):
    return len(s)

stringsub = {
    "1": "100",
    "0": "111"
}






