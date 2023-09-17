#Dictionaires
defined = {
    "primary_cost": "Direct Materials and Direct Labor",
    "conversion_cost": "Direct Labor and Man Overhead",
    "contribution_margin": "Sales - All Varible Expenses",
    "COGM": """   RAW MATERIALS         WORK IN PROGRess       
                + BEG RM                + BEG WIP
                + RM Purchased          + Total Manuf Cost (RM USED + DIRECT LABOR + OH)
                -------------           -----------
                RM Availible            Total WIP
                - Ending RM             - Ending WIP
                -------------           -------------
                 RM Used                 COGM
                       """,
    "COGS": """+ Beg Finished Good
               - Ending Fin Goods 
               + COGM
               = Adjusted COGS"""

}

while True:
    needed = ""
    response = ""
    answer = ""
    user_start = input("Definition? or Find_Overhead? ")

    if user_start.lower() == ("definition"):
        answer = input("Definition Required? = primary_cost, conversion_cost, contribution_margin, COGM or COGS : ")

    if answer in defined:
        print ("Definition is", defined[answer])
        response = input("Do we need to calculate anything?")

# checking this response
    if response.lower() == "yes":
        needed = input("What is needed? COGM or COGS: ")
#elif response.lower() == "no":
   # print ("All Done")

    if needed.upper() == "COGM":
    # takes the needed values to find COGM or COGS
        print ("We need to start of with RM Schedule")
        beg_RM = int(input("Enter Beg RM: "))
        RM_purchases = int(input("Enter RM Purchases: "))
        RM_Available = beg_RM + RM_purchases
        End_RM = int(input("Enter End RM: "))
        RM_Used = RM_Available - End_RM
        print ("RM Used is :", RM_Used)
        Manufacting_Overhead = int(input("Manufacting Overhead: "))
        Dir_Lab = int(input("Direct Labor: "))
        Total_Man_Cost = RM_Used + Dir_Lab + Manufacting_Overhead
    # Now Creating Work in Progress Schedule
        beg_wip = int(input("BIG_WIP: "))
        end_wip = int(input("END WIP: "))
        print ("COGM = ", (beg_wip + Total_Man_Cost - end_wip))

    elif needed.upper() == "COGS":
        beg_fin = float(input("Enter Finished Goods: "))
        end_fin = float(input("Enter Ending Finished Goods: "))
        cogm = float(input("Enter Cost of Goods Manufactured: "))
        cogs = (beg_fin + cogm - end_fin)
        print (f"COGS = {cogs}") # THis isnt Printing
    else:
        miss_type = ("Miss Type? Type COGM or COGS")



# Calculate POHR,MAN OVER, AND APPLIED, AND DETERMINE IF OVER/UNDER
    response_2 = ""
#print ("Please enter all values.")
    if user_start.lower() == ("find_overhead"):
        Est_OH = float(input("Enter Estimated Overhead: "))
        Est_DLA = float(input("Enter Estimated Denominal Level of Activity: "))
        Est_Var = float(input("Enter varible overhead per unit(if none put 0):"))
        Est_Var_Act = float(input("Enter DLA of Varible(if none put 0):"))
        POHR_Rate = (Est_OH + (Est_Var * Est_Var_Act)) / (Est_DLA)
        print (f"The POHR rate is {POHR_Rate}.")
        response_2 = input("Would you like to check if over and under? Yes or No? ") # should probalu ask for oh applied

# Ask to find OH APPLIED VS ACTUAL

    if response_2.lower() == "yes":
        Actual = float(input("Enter Actual Overhead: "))
        Actual_DLA = float(input("Actual DLA: "))
        OH_Applied = POHR_Rate * Actual_DLA
        diff = OH_Applied - Actual
        print (f"The Overhead Applied {OH_Applied}.")
        if diff > 0:
            print (f"""We are overapplied by {abs(diff)}
                                Overhead {abs(diff)}
                                    COGS GOES DOWN {abs(diff)} """ )
        elif diff < 0:
            print (f"""We are underapplied by {abs(diff)}
                                COGS GOES UP {abs(diff)}
                                    Overhead {abs(diff)}""")
        if response_2.lower() == "no":
            continue
    end_function = input("Stop or Continue? ")
    if end_function.lower() == "stop":
        break

