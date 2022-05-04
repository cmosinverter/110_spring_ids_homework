def In2Post(expression):
    post = []
    stack = []
    for item in expression:
        if item in 'ABCDE':
            post.append(item)
        if item == '(':
            stack.append(item)
        if item in '*/':
            while(stack):
                if stack[-1] in '(+-':
                    break
                else:
                    a = stack.pop()
                    post.append(a)
            stack.append(item)
                
        if item in '+-':
            while(stack):
                if stack[-1] in '+-*/':
                    a = stack.pop()
                    post.append(a)
                else:
                    break
            stack.append(item)
                    
            
        if item == ')':
            while (stack[-1]!='('):
                a = stack.pop()
                post.append(a)
            stack.pop()
    while(stack):
        a = stack.pop()
        post.append(a)
    return post

def Calculate(postfix, num_list):
    stack = []
    for item in postfix:
        if 65 <= ord(item) <= 69:
            stack.append(num_list[ord(item)-65])
        if item == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append((b+a))
        if item == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append((b-a))
        if item == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append((b*a))
        if item == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b/a))
    return print(stack[0])
    




expression = list(input())
n = int(input())
postfix = In2Post(expression)
for i in range(n):
    num = list(map(int, input().split()))
    Calculate(postfix, num)
