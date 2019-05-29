def bubble_sort(arr):
    
    n = len(arr)
    
    for i in range(n):
        
        for j in range(n-i-1):
            
            if arr[j+1] < arr[j]:
                
                arr[j], arr[j+1] = arr[j+1], arr[j] 
    
    print(arr)
    
if __name__ == '__main__':
    
    arr = [5,4,3,2,1]
    
    bubble_sort(arr)    