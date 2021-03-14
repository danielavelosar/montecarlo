
def bestSum(target, array, memo={}):
  if target==0: return []
  if target<0: return None
  try: return memo[target]
  except KeyError:

    shortest_combination = None 
    for number in array:
      reminder=target-number
      reminder_result=bestSum(reminder,array, memo)
      if (reminder_result) is not None:
        new_array= reminder_result
        new_array.append(number)
        shortest_combination= new_array
        if len(new_array) <= len(shortest_combination):
          shortest_combination=new_array
          
          
    
    memo[target]=shortest_combination
    return shortest_combination

if __name__== '__main__':
    print(bestSum(100, [1,100,50]))