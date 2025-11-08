def solve(N: int, C: list, P: list) -> str:
#     """
#     Return a single string of the champion's name
    
#     N: The length of C and P
#     C: List of strings of the competitors
#     P: List of integers of competitor's power
#     """
# SOLUTION:
      # let me make pairs of the competitors to fight each other
      comp_pairs = [(C[i],P[i]) for i in range(N)]
      # DO THE FOLLOWING TILL:
      while len(comp_pairs)>1:
          
          # will store the intermediate champions for the next round of fight
          nextRound = []
          for i in range(0,len(comp_pairs),2):
              # now i will have two competitors
              competitor1, competitor2 = comp_pairs[i],comp_pairs[i+1]
              
            # compare comp1 and comp2
              if competitor1>competitor2:
                  # add powers
                  power = competitor1[1] + competitor2[1]
                  # update the nextRound with:
                  nextRound.append((competitor1[0],power))
              elif competitor1<competitor2:
                  power = competitor1[1] + competitor2[1]
                  nextRound.append((competitor2[0],power))
              else:
                  # we got the same powers so:
                  superFighter = competitor1[0] + competitor2[0]
                  superPower = competitor1[1]+ competitor2[1]
                  nextRound.append((superFighter,superPower))

          comp_pairs = nextRound
          # i just need the name of the champion
      champion = comp_pairs[0][0]
      
      return champion
                 

#     return champ



def main():
    T = int(input())
    for _ in range(T):
        N = int(input()) 
        C = input().split(" ")
        P = list(map(lambda s: int(s), input().split(" ")))
        print(solve(N, C, P))

if __name__ == '__main__':
    main()
