def solve(N: int, M: int, P: list[str], C: list[str]):
    """
    Output a possible configuration of the chest after performing quickstack

    N: the number of items the player has
    M: the number of items the chest has
    P: the list of items on the player
    C: the list of items in the chest
    """
    # YOUR CODE HERE
    combined_str = P + C
    combined_str.sort()
    return combined_str


def main():
    T = int(input())
    if 1 <= T and T <= 100:
        for _ in range(T):
            info = input().split(' ')
            N, M = int(info[0]), int(info[1])
            if (1 <= N and N<= pow(10,5)) and (1 <= M and M<= pow(10,5)):
                P = [x for x in input().split(' ')]
                C = [x for x in input().split(' ')]
                result = solve(N, M, P, C)
                print(' '.join(result))
    


if __name__ == '__main__':
    main()