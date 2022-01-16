#this learning topic is on input functions
name = input (' Whats your name?')
hours_worked = float (input ('How many hours did you work?'))
regular_pay = hours_worked * 18
overtime_pay = (hours_worked -40) *18 *1.5
total_pay = regular_pay + overtime_pay
if hours_worked <= 40 :
  print ('your wage was =', regular_pay)




  print  ('============================================')
  user_age = input ('How old are you?')
  if ((user_age >= 8) and (user_age <= 12)) :
    print ("you are allowed, welcome")
  else : print ("sorry you are not allowed bye!")
