def infix_to_RPN(inp):
    precedence = ["~","^","/","*","+","-"]
    RPN_order = []
    for i in range(len(inp)):
        if inp[i] not in precedence:
            RPN_order.append(i)
        else:
            RPN_order.append(inp[i+1])
            #inspect
            if precedence.index(inp[i]) < precedence.index(inp[i+2]):
                RPN_order.append(inp[i])
            else:
                RPN_order.append(inp[i+2])