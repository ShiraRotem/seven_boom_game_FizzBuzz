def seven_boom():
    user_turn = True
    number = 0
    for num in range(2,22):
        number += 1
        if (user_turn):
            order = (input("put in the next number and press the 'enter' key"))
            if order.isdigit():
                if (int(order) != number):
                    print("NOT the right number, YOU LOSE!")
                    break
                elif (int(order) == number):
                    if ((number) % 7 != 0):
                        (order)
                    elif ((number) % 7 == 0):
                        print("Should be Boom, YOU LOSE!")
                        break
            elif (str(order) == ("Boom!")):
                if ((number) % 7 != 0):
                    print("This number does not divide by 7, YOU LOSE!")
                    break
                else:
                    print("Very Good!")
                    (order)
            else:
                print('Wrong answer, answer should be "Boom!", try again')
                break
        else:
            if ((number) % 7 == 0):
                print("Computer says: {0}".format("Boom!"))
            else:
                print ("Computer says: {0}".format(number))
        user_turn = not user_turn
    print ("Game ended!")

print (seven_boom())

