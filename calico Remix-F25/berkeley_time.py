def solve(N: int) -> str:
    """
    Return the appropriate text given the contest will start N minutes late.
    
    N: the number of minutes late the contest will start
    """
    # YOUR CODE HERE
    mesg = "berkeleytime"
    prefix = ""
    if N < 10:
        mesg = "haha good one"
        return mesg
    elif N>= 10 and N < 180 :
        multiplier = N//10 -1
        prefix =("berkeley" * multiplier)
        mesg = prefix + mesg
        return mesg

    else:
        mesg = "canceled"
        return mesg


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(solve(N))


if __name__ == '__main__':
    main()
