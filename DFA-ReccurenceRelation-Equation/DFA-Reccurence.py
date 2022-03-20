# Members: Jacob Rosner, Andrew McKernan, Samuel Ortega Gonzalez

# Andrew's Contribution
# Summary: Part 1 of the project, returns the number of possible valid encodings
# of length N for a predetermined DFA M. Where the languages is 
# {A,B,C,D} and a valid encoding of length n contains at least each 
# symbol once.
# Param n: the length of a substring for each valid encoding
# Return: The number of valid encodings of length n
def count(n):
  curr = {'DEAD': 
       {
        'delta': ['DEAD','DEAD','DEAD','DEAD'],  #Hardcoded DeadState
        'J': 0                        
      }
  }
  buildDFA(curr)
  next = {}

  #uses the recurrence relation to compute number of valid encodings
  for c in range(0,n):
    for key in curr:
      temp = 0

      for s in range(0,4):
        temp = temp + curr[curr[key]['delta'][s]]['J']
      next[key] = {'delta':curr[key]['delta'], 'J':temp}
    
    for key in curr:
      curr[key]['J'] = next[key]['J']
    
    for key in curr:
      next[key]['J'] = 0
      
  return curr['']['J']
 
# Summary: Recursive element of count
# Param n: the length of a substring for each valid encoding
# Param buffer: the five most recent letters used
# Return: the sum of the number of valid encodings
def buildDFA(m):
  #language
  L = ['A','B','C','D']
  idxValues = ['']
  buildAllStateValues(idxValues, L)
  
  for i in range(len(idxValues)):
    buffer = idxValues[i]
    
    #340 is hardcoded value for number of inputs with length < 6 (not full)
    if i <= 340:
      m[idxValues[i]] = {'delta':[idxValues[i] + 'A',idxValues[i] +'B',
                                  idxValues[i] + 'C',idxValues[i] + 'D'], 
                         'J': 1}
    else:
      bufferDict = {'delta':['DEAD','DEAD','DEAD','DEAD'], 'J' : 1}
        
      #assign valid delta paths
      for letter in L:
        if(isValidEncoding(buffer + letter)):
          bufferDict['delta'][L.index(letter)] = (buffer[1:] + letter)
        
      m[buffer] = bufferDict


# Summary: helper function to see if substring is accepeted by DFA M
# Param value: specific letter + buffer we are evaluating
# returns: True if substring is accepted, else false
def isValidEncoding(value): 
  if (value.find('A') == -1):
    return False
  if (value.find('B') == -1):
    return False
  if (value.find('C') == -1):
    return False
  if (value.find('D') == -1):
    return False
  return True

# Summary: helper function to create all state combinations
# Param arr: this is the array of all values that is continuously built
# Param language: this is the list of all valid symbols
def buildAllStateValues(arr,language):
  buildStateLength(language, "", 1, arr)
  buildStateLength(language, "", 2, arr)
  buildStateLength(language, "", 3, arr)
  buildStateLength(language, "", 4, arr)
  buildStateLength(language, "", 5, arr)

# Summary: helper function to create a single state combination of length k
# Param language: this is the list of all valid symbols
# Param prefix: specific character that we are appending
# Param k: idx value in string we are at
# Param arr: this is the array of all values that is continuously built
def buildStateLength(language, prefix, k, idxValArr):
	if (k == 0):
		idxValArr.append(prefix)
		return
	for i in range(4):
		newPrefix = prefix + language[i]
		buildStateLength(language, newPrefix, k - 1, idxValArr)

#Jacob Rosner Question 2 2/28/22
from queue import Queue
def Delta(i, a, k):
  #i is the current state
  #a is the input symbol
  #k is the input
  return ((10 * i) + a) % k

def FindString(k, D):
  q = Queue()
  VISITED = []
  FINAL = []
  LABEL = []
  PARENT = []
  found = False
  for i in range(0, k):
    VISITED.append(False)
    LABEL.append(None)
    PARENT.append(None)

  for i in D:
    if (i != 0):
      q.put(i)
      VISITED[i] = True
      PARENT[i] = 0
      LABEL[i] = i

  while q.empty() == False:
    current = q.get()
    for i in D:
      next = Delta(current, i, k)
      if (current == 0):
        found = True
        break
      else:
        if (VISITED[next] == 0):
          PARENT[next] = current
          VISITED[next] = True
          LABEL[next] = i
          q.put(next)
  if (found == False):
    return "No Solution"
  else:
    string = str(LABEL[0])
    check = PARENT[0]
    while(check != 0):
      string = string + str(LABEL[check])
      check = PARENT[check]
  string = string[::-1]
  return string

# Samuel's text base UI options

def main():
  answer = 0
  
  while (answer != 3):
    print("*******************************************")
    print("* Welcome to project 1! What\'ll it be?    *")
    print("* 1. Problem 1                            *")
    print("* 2. Problem 2                            *")
    print("* 3. Exit program                         *")
    print("*******************************************\n")
    answer = int(input())
    
    # Problem 1
    if answer == 1:
      print("\n*******************************************")
      print("* You have chosen option 1!               *")
      print("*                                         *")
      print("*******************************************\n")

      print("input an integer")
      n = int(input())
      result = count(n)
      print("Result:", result)
      continue
    
    # Problem 2
    elif answer == 2:
      print("\n*******************************************")
      print("* You have chosen option 2!               *")
      print("*                                         *")
      print("*******************************************\n")

      global isValid

      while (True):
        kString = int(input("Enter a positive integer of k > 0: "))
        
        # Check if K input > 0
        if kString <= 0:
          print("Error: Cannot input 0. Please try again.\n")
          continue

        subsetList = list(map(int, input("Digits permitted: ").split()))

        # Check to make sure all inputs > 0
        if(subsetList[0] == 0 and len(subsetList) == 1):
          print("No Solution")
          isValid = False
          break
        else:
          isValid = True

        # Check if inputs are all valid. If True, call function.
        if isValid == False:
          continue

        else:
          # Call function
          print("Result:", FindString(kString, subsetList))
          break
      continue

    # Exit program
    elif answer == 3:
      print("\n*******************************************")
      print("* You have chosen option 3!               *")
      print("* Ending program...                       *")
      print("*******************************************\n")
    
    # Invalid
    else:
      print("Invalid option! Try again")

main()
