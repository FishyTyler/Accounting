
from operator import truediv

defined = {
    "activity_rate": "(POHR RATE): Estimated Overhead / DLA",
    "units_comp": "Units out - units beg inv",
    "EU_END_WIP": "% Complete * End Wip",
    "End_Cost_Unit": "Equivilant Units in WIP * Cost per Equilivant Unit",
    "FIFO_EU": """  FOR FIFO
                  1: EU to finish BWIP - (Beg Units * (1 - % Complete))
                  2: Units 100% During Month (Units out - Unit Beg Inv)
                  3: EU in End WIP (% Complete * End WIP)
                  Cost per equilivant unit = (Cost added during the period)/ Equivalent units of production""",
    "cost_accounted": "Beg WIP + Cost added to Production"
}
# Defined function for POHR RATE or Activity base
def find_activity_rate(est_oh, est_dla):
    return est_oh / est_dla
# Defined function to find OH per unit based on DLA
def oh_assigned(rate, direct_hrs_per):
    return rate * direct_hrs_per
def labor_cost(cost, direct_hrs_per_unit):
    return cost * direct_hrs_per_unit

# takes a dictionary in a list format
key_list = list(defined.keys())

while True:
    ABC_activity_list = []
    ABC_Expected_Activity = []
    final_activity_list = []
    user_input = input("Definition or Find_Overhead or ABC: ")
    if user_input.lower() == "find_overhead":
        pohr_rate = find_activity_rate(float(input("Enter Estimated Overhead Cost: ")), float(input("Enter Expected DLA: ")))
        pohr_rate = round(pohr_rate, 2)
        print(f"The POHR rate is: ${pohr_rate}")
        user_continue = input("Find Specific  OH Unit Product Cost: Yes or NO? ")
        if user_continue.lower() == "yes":
            lbr_hrs = float(input("Enter Labor Hrs Per unit"))
            Assigned_OH = oh_assigned(pohr_rate, lbr_hrs)
            print (f"The assigned OH is, ${Assigned_OH}.")
            find_labor_cost = labor_cost(float(input("Enter wage rate: ")), lbr_hrs )
            print (f"The total labor cost is: ${find_labor_cost}.")
            DM_Cost_per = float(input("Enter DM Cost per Unit: "))
            Total_unit_cost = (Assigned_OH + find_labor_cost + DM_Cost_per)
            print (f"The total per unit cost is ${Total_unit_cost}.")
    elif user_input == "ABC": # Setting activity rates
        num_inputs = int(input("Enter # of activites: "))
        ABC_activity_list = []
        ABC_Expected_Activity = []
        final_activity_list = []
        for i in range(num_inputs):
            user_activity_input = int(input(f"Enter Estimated OH Activity {i+1}: "))
            ABC_activity_list.append(user_activity_input)
            user_expected_activity = float(input(f"Enter TOTAL Expected Level of Activity {i+1}: "))
            ABC_Expected_Activity.append(user_expected_activity)

        print (ABC_activity_list)
        print (ABC_Expected_Activity)
        divided_values = (list(map(truediv, ABC_activity_list, ABC_Expected_Activity)))
        print (divided_values)
        
        ABC_OH_Assigned = []
        for i in range(num_inputs):
            final_activity_input = float(input(f"Enter actual #'s of activity {i+1}: "))
            final_activity_list.append(final_activity_input)
            ABC_OH_Assigned.append(divided_values[i] * final_activity_list[i])
            Final_ABC_Assigned = sum(ABC_OH_Assigned)
            print (ABC_OH_Assigned)
        num_of_units = float(input("Enter number of units per product: "))
        final_per_unit = (Final_ABC_Assigned / num_of_units)
        print (f"The sum of the ABC OH is: {Final_ABC_Assigned} and per unit is: {final_per_unit}")

        """for values in range(num_inputs):
            final_activity_input = float(input(f"Enter actual #'s of activity {values+1}: "))
            final_activity_list.append(final_activity_input)
            ABC_OH_Assigned = (list(map(truediv,divided_values * final_activity_list)))
        print (f" The OH assigned is {ABC_OH_Assigned}")"""


        #WE need to divide each list by the other list


    elif user_input.lower() == "definition":
        print(f"Definitions Available: {key_list}")
        answer = input("What is needed? : ")
        if answer in defined:
            print("Definition is,", defined[answer])
    end_function = input("Stop or Press Enter: ")
    if end_function.lower() == "stop":
        print ("All done.")
        break
