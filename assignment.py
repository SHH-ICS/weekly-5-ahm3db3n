def calculate_pi(iterations):
    pi=0
    for i in range(iterations)
    term=(-1)**i / (2*i+1)
    pi+= term return pi * 4
    
    try:
    
    iterations = int(input("Enter the number of iterations"))
    if iterations <=0:
        print ("Errror Please enter a positive integer.")
        else:
        pi_value = calculate_pi(iterations)
        print(f"the calculated value of pi is {pi_value}")
        except ValueError:
        print("error: Please enter a vald number")