def solve(N: int, P: str) -> int:
    """
    Return the total money Big Ben pays
    
    N: length of the string P
    P: string of characters representing the people Big Ben talks to
    """
    # YOUR CODE HERE
    money = 0 
    increment = 1
    for i in range(N):
        # print(i)
        if P[i] == 'T':
            money = money + 1 * increment
            increment = 1
        elif P[i]=='D':
            increment = increment * 2
    # now return the money
    return money

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = input().upper()
        print(solve(N, P))

if __name__ == '__main__':
    main()
