
def convert_pounds(pounds):
    kg = pounds * 2.20462
    print(pounds," kilograms are ",kg, " pounds")

def convert_kg(kg): 
    pounds = kg *  0.453592
    print(kg," pounds are ",pounds, "kilograms")

if __name__ == "__main__":
    kg = 80
    pounds = 150
    convert_kg(pounds)
    convert_pounds(kg)
        