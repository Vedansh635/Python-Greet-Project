import time , pyttsx3 as pyvoice
engine = pyvoice.init()

# All Question included here and will include here
questions = ["""Q.1 What is the full form of 'LOL' ?" \n
              (a)Loud on laugh (b)Loud of laugh (c)Letter of letter (d)None of these""",
             """Q.2 What is the first planet in our solar system ? \n
             (a)Mercury (b)Jupiter (c)Pluto (d)Venus""",
             """Q.3 What is the closest star to earth ? \n
             (a)Proxima Centauri (b)Sun (c)Vega (d)Rigel""",
             """Q.4 Which is hottest planet in our solar system ?\n
             (a)Mercury (b)Venus (c)Mars (d)Earth""",
             """Q.5 Which is largest galaxy in our universe ?\n
             1.Milky way (b)Andromeda (c)Vigro Cluster (d)IC 1101"""
             ]

# Main variable that holds prize
Price_money = 0

#                                 --------------functions------------
def nextquesanim():
    print("Next question coming" , end="")
    time.sleep(0.5)    
    print(".",end="")
    time.sleep(0.5)    
    print(".",end="")
    time.sleep(0.5)    
    print(".",end="\n \n \n \n \n")
    time.sleep(0.7)

    
def question_sys(question,correct_ans_value,Prizemoney_incre):
      global Price_money
      engine.say(f"This question For {Prizemoney_incre} dollar ")
      engine.runAndWait()
      print(f"THIS QUESTION FOR ${Prizemoney_incre} ")
      print(questions[question])
      correct_ans = input().lower()
      if correct_ans == correct_ans_value:
          Price_money+=Prizemoney_incre
          print(f"The answer is correct you won ${Prizemoney_incre}! TOTAL POOL => ${Price_money}")

      elif  correct_ans >= "e" or not(correct_ans.isalpha()):
           print("Option Not Included !!")     

      else:
         print("Wrong answer!!")
      if question < len(questions) - 1:
        nextquesanim()
def result():
    if Price_money > 100:
       engine.say(f"Congo! You win total {Price_money} dollars")
       engine.runAndWait()
    print(f"You win total ${Price_money}")


# ---Actual_Working---

# Q.1
question_sys(0,"a",100)


# Q.2
question_sys(1,"a",1000)

# Q.3
question_sys(2,"b",10000)

# Q.4
question_sys(3,"b",25000)

# Q.5
question_sys(4,"d",50000)

result()