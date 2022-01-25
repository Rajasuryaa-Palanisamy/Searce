
def getMax(operations):
    stack = []    
    max_elem = 0
    
    for _ in range(operations):
        args = list(map(int, input().strip().split()))
        
        if args[0] == 1:
            max_elem = max(max_elem, args[1])
            stack.append(args[1])
        if args[0] == 2:
            if stack.pop() == max_elem:
                if len(stack) > 0:
                    max_elem = max(stack)
                else:
                    max_elem = 0
        if args[0] == 3:
            print(max_elem)
            
operations = int(input().strip())
getMax(operations)
