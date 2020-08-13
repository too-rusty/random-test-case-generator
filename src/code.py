
def two_sum():
    def solve():
        n, target = map(int, input().split(" "))
        a = list(map(int , input().split(" ")))
        for i,x in enumerate(a):
            for j in range(i+1,n,1):
                if x + a[j] == target:
                    print (i,j)
                    return None
        print (-1,-1)

    t = int(input())
    for _ in range(t):
        solve()

def main():
    pass

if __name__ == '__main__':
    # write only a single function here
    # that needs to be executed
    two_sum()