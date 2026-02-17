def spin_twister_spinner():
  """
  Returns a list with a random color, side, and appendage
  
  colors: "red", "green", "yellow", or "blue"
  sides: "left" or "right"
  appendage: "hand" or "foot"
  """
  import random
  colors = ["red", "green", "yellow", "blue"]
  w = random.choice(colors) 
  sides = ["left", "right"]
  x = random.choice(sides) 
  appendage = ["hand", "foot"]
  z = random.choice(appendage) 
  return w, x, z 

# Here's the function call. This should print a random assortment of twister commands
for _ in range(10):
  print(spin_twister_spinner())