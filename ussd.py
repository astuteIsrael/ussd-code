ussd_code = input("Enter your ussd code ")
if ussd_code == "#321":
    print("1. Data Plans\n2. Get 3GB + 5 voice mins for N1,200\n3. Social Bundles\n4. Business Plans\n5. Roaming/Int'l\n6. Borrow Credit/Recharge\n0. Next")
    options = input("Enter the number of your choice")
    if options == "1":
        Plans = input("Please enter your plan ")
        if Plans == "daily":
            print("1. Data Plans\n2. Get 3GB + 5 voice mins for N1,200\n3. Social Bundles\n4. Business Plans\n5. Roaming/Int'l\n6. Borrow Credit/Recharge\n0. Next")        
        elif options =="weekly":
             print("1. Data Plans\n2. Get 3GB + 5 voice mins for N1,200\n3. Social Bundles\n4. Business Plans\n5. Roaming/Int'l\n6. Borrow Credit/Recharge\n0. Next")
        else:
            print("Your course is not here, go to the frontdesk")
    elif options == "Get 3GB + 5 voice mins for N1,200":
        payment = input("Do you want to purchase this plan now? ")
        if payment == "yes":
            print("You have subscribed for this bundle")
        else:
            print("check other options")

    elif options == "Social Bundles":
        payment = input("Do you want to purchase this plan now? ")
        if payment == "yes":
            print("1. whatsapp\n2. instagram\n3. TT/YT/IG")
        else:
            print("check other plans")

    elif options == "Business Plans":
        payment = input("Do you want to purchase this plan now?  ")
        if payment == "yes":
            print("You have subscribed for this bundle")
        else:
            print("check other plans")

    elif options == "Roaming/Int'l":
        payment = input("Do you want to purchase this plan now? ")
        if payment == "yes":
            print("This plan currently not available!!")
        else:
            print("check other plans")
    elif options == "Borrow Credit/Recharge":
        payment = input("Do you want to borrow airtime/data ")
        if payment == "yes":
            print("1. N2000\n2. N1000\n3. N750\n4. N500\n5. Borrow Data\n6. More XtraTime\n7. MoreTime\n8. Next")
        else:
            print("Check other plans")
    
    else:
        print("check code again")
else:
    print("wrong code!!")
    