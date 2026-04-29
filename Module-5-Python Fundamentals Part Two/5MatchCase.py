color = input("color match : ")


match color:
    case "green":
        print("Go")
    case "red":
        print("stop")
    
    case "yellow":
        print("stop")
    #defult
    case _:
        print("wrong colro ")