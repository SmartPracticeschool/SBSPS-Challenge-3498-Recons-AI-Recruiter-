import pandas as pd
def chat():

    welcome_msg = print("Welcome to Recons Recruitment Assistane!\nI am here to interview you. Your answers will decide your rank among all candidates and then you will be called for walk-in-interview. Best wishes! ")
  
    name = input("May I have your name please? ")
    
    q1 = print("Great! " + str(name) + "! Now, I will ask you some questions to test your personality and aptitude. ")
    
    q2 = input("Select a position you would prefer to work for:- \n [a]---\n[b]---\n[c]---")
    
    q2 = input("Tell Me About Yourself.")
    
    q3 = input("Why Should We Hire You?")
    
    q4 = input("What Are Your Greatest Strengths?")
    
    q5 = input("What Do You Consider to Be Your Weaknesses?")
    
    q6 = input("What Is Your Greatest Professional Achievement?")
    
    q7 = input("Why Are You Leaving Your Current Job? If any")
    
    q8 = input("What Do You Like Least About Your Job?")
    
    q9 = input("What Are You Looking for in a New Position?")
    
    q10 = input("What Are You Passionate About?")
    
    q11 = input("What’s Your Dream Job?")
    
    q12 = input("What Should I Know That’s Not on Your Resume?")
    
    q13 = input("What Are Your Salary Requirements?")
    
    q14 = input("When Can You Start?")
    
    user_response = input("Do you have any questions for me? ")
    
    print("""
    Recons Technologies Pvt Ltd.
    Experience - 0-4 years
    Salary- 150000-450000
    Location-Pune
    Role- Software Developer
    Skills - Python
    Education- B.E/B.Tech in CS/ Equivalent 
    Contact- www.recons.online
    Write us at reconsmit@gmail.com if you have any questions.
    """)
    
    emailid = input("Share your Email-ID")


    ls=[name,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,user_response,emailid]
    df=pd.DataFrame(ls).T
    df.to_csv('Users_Response.csv', index=True, header=True)


    return print("You will receive an email for walk-in-interview, incase you get selected. On- " + str(emailid) + "\nThank you!" )



chat() 

        


