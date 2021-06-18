# Write your code here
def convert_miles(km):
    miles = km * 0.62
    print(km,"kilometers are ",miles, "miles")

def convert_km(miles): 
    km = miles * 1.61 
    print(miles,"miles are ",km, "kilometers")

if __name__ == "__main__":
    km = 10
    miles = 3
    convert_km(miles)
    convert_miles(km)
        