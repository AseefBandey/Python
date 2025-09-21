# Input Format: N = 3
# Result: 
# 1
# 1 2 
# 1 2 3

# n = int(input("Enter N: "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j ,  end="")
#     print()

# Input Format: N = 3
# Result: 
# 1 2 3
# 1 2
# 1

# n = int(input("Enter N: "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# Input Format: N = 3
# Result: 
#   *  
#  *** 
# ***** 


# n = int(input("Enter N: "))


# for i in range (1, n+1):

#     spaces = n - i
#     print(" " * spaces,end="")


    stars = 2 * i - 1
    print("*" * stars)

