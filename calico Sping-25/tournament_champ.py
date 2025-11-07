competitors = input().strip().split()
powers = list(map(int,input().strip().split(" ")))

# print(type(powers))
champion = [(competitors[i],powers[i]) for i in range(len(powers))]

while len(champion)>1:
   nextRound =[]
   for i in range(0,len(champion),2):
      comp1, comp2 = champion[i],champion[i+1]
      if comp1[1]>comp2[1]:
         nextRound.append((comp1[0],int(comp1[1]+comp2[1])))
      elif comp1[1]<comp2[1]:
         nextRound.append((comp2[0],int(comp1[1]+comp2[1])))
      else:
         superGuy = comp1[0]+comp2[0]
         # but I need to add the powers too, and add to the newly superGuy
         superPower= int(comp1[1]+comp2[1])
         nextRound.append((superGuy,superPower))
   champion = nextRound

print(champion[0][0])

# def solve(N: int, C: list, P: list) -> str:
#     """
#     Return a single string of the champion's name
    
#     N: The length of C and P
#     C: List of strings of the competitors
#     P: List of integers of competitor's power
#     """
#     # YOUR CODE HERE
#     # champ = C[P.index(max(P))]
#     champ  = list()

#     for i in P:
#         if i>=i+1:
#             P.pop(i+1)
#         elif i<=i+1:
#             P.pop()

#     return champ
# # try this also
#     # return C[P.index(max(P))]


# def main():
#     T = int(input())
#     for _ in range(T):
#         N = int(input())
#         C = input().split(" ")
#         P = list(map(lambda s: int(s), input().split(" ")))
#         print(solve(N, C, P))

# if __name__ == '__main__':
#     main()
