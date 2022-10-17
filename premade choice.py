#First menu (everything will be added at the end)
print("Hello there, welcome to Best Buy. I'm a chatbot that will be helping and guiding you throughout the process, how may I help you?")
print("""
1. Creat your own pc
2. Premade Pc's
3. Locations
4. Work for us
""")
ans = input("Please pick an answer: ")
if ans == "1":
    print("\n")
elif ans == "2":
    #Premades only (redirections later)
    print("Would you like suggestions and guidance to what to get depending on type of work?")
    print("""
    1. Yes
    2. No
    """)
    ans1 = input("Please pick an answer: ")
    if ans1 == "1":
        print("What would the field of work be?")
        print(""""
        1. Teacher
        2. Student
        3. Programmer
        4. Gaming
        5. Data entries
        """)
        ans2 = input("Please pick an answer: ")
        if ans2 == "1":
            print("Perfect! Here are some options that would be compatable: ")
            print("""
            1. Dell Optiplex 9020
            2. Apple iMac 27-inch Desktop (aimed at visiual thinking teachers)
            3. Dell Inspiron
            """)
            ans3 = input("Please pick an answer: ")
            if ans3 == "1":
                print("\n")
            elif ans3 == "2":
                print("\n")
            elif ans3 == "3":
                print("\n")
            elif ans3 == "":
                print("\n Invalid answer, try again.")
        elif ans2 == "2":
            print("\n")
        elif ans2 == "3":
            print("\n")
        elif ans2 == "4":
            print("\n")
        elif ans2 == "5":
            print("\n")
        elif ans2 != "":
            print("\n Invalid answer, try again.")
    elif ans1 == "2":
        print("Here is a list of our top sellers: ")
        print("""
        1. HP OMEN - 40L Gaming Desktop - Intel Core i7-12700KF - HyperX 16GB Memory - NVIDIA GeForce RTX 3060 Ti - 1TB SSD - Nightfall Black
        2. iBUYPOWER TraceMR Gaming Desktop - AMD Ryzen 5600X - 16GB DDR4 Memory - AMD RX 6600 XT - 1TB HDD + 500GB NVMe SSD - Black
        3. Skytech Gaming - Chronos Mini Gaming Desktop - Intel i5-10400F - 16G 3200 Memory - NVIDIA GeForce GTX 1660 Super - 500G SSD - Black
        4. CyberPowerPC - Gamer Master Gaming Desktop - AMD Ryzen 5 5600G - 16GB Memory - NVIDIA GeForce RTX 3060 - 2TB HDD + 500GB SSD - White
        """)
    elif ans1 != "":
        print("\n Invalid answer, try again.")
elif ans == "3":
    print("\n")
elif ans == "4":
    print("\n")
elif ans != "":
    print("\n Invalid answer, try again.")