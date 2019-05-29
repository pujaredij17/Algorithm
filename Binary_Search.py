def normal_search(l, x):
  for element in l:
    if element == x:
      return True
  return False

def binary_search(l, x):
    start = 0
    last = len(l)
    
    while True :
        mid = (start + last) // 2
    
       # print(mid)
      #  print(l[mid])
       # print(x)
      
        if (x < l[mid]):
            last = mid
        
        elif x > l[mid]:
            start = mid
        
        elif x == l[mid]:
            return True
        
        return False   
          
           
if __name__=="__main__":
  l = [2, 4, 6, 8, 10]
  print(normal_search(l, 6)) # prints False
  result = (binary_search(l, 11))
  
  print(result)