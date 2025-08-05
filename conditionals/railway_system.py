category = input("Enter your seat type (sleeper , ac , genreal , luxury) : ").lower()

match category :
    case "sleeper":
        print("You have a seat and your time ")
    case "ac":
        print("You got thandi thandi hawa and kanch ka glass")
    case "Genereal" :
        print("You poor human")
    case "luxury" :
        print("Bhai ke aish hai ") 
    case _ :
        print("Invalid type of category ")     
        