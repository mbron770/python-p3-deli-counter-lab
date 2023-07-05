katz_deli = []

def line(katz_deli):
  if not katz_deli:
      print('no line')
  else: 
      message = 'line at: '
      for i in range(len(katz_deli)):
          message += f'{i+1} {katz_deli[i]}'


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f'Welcome, {name}. You are {len(katz_deli)} in line')
    
    
def now_serving(katz_deli):
    if not katz_deli: 
        print("There is nobody waiting to be served!")
    else: 
        print(f'currently serving: {katz_deli[0]}')
        del katz_deli[0]
    















# message += f'{i+1}. {katz_deli[i]}'
