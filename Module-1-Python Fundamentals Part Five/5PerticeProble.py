
data = True 

with open("Python Fundamentals Part Five/sample.txt", "r") as f :
    while data :
        data = f.readline()
        if("Python" in data):
            print("python word find")
            print(data)