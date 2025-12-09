no = [10, 20, 30, 40, 50]
print("initial list",(no))
no[1]=200                   #Change Element
print("after changing second element",(no))

no.append(600)              #Append Element
print("after apending 600",(no))

no.insert(2,300)            #insert Element
print("after inserting 300 at the third position",(no))

no.remove(600)              #remove Element by value
print("after removing 600 ",(no))

no.remove(no[0])            #remove Element by index
print("after removing element at 0 ",(no))



