def two_sum():
    def solve():
        n, target = map(int, input().split(" "))
        a = list(map(int, input().split(" ")))
        for i, x in enumerate(a):
            for j in range(i + 1, n, 1):
                if x + a[j] == target:
                    print(i, j)
                    return None
        print(-1, -1)

    t = int(input())
    for _ in range(t):
        solve()


def count_and_say():
    def solve():
        n = int(input())
        now = '1'
        prev = now[:]
        for i in range(2, n + 1, 1):
            cnt = 1
            c = prev[0]
            now = ''
            for i in range(1, len(prev), 1):
                if prev[i] == prev[i - 1]:
                    cnt += 1
                else:
                    now += cnt.__str__() + c
                    c = prev[i]
                    cnt = 1
            now += cnt.__str__() + c
            prev = now[:]
        print(now)

    t = int(input())
    for _ in range(t):
        solve()


def main():
    pass


if __name__ == '__main__':
    # write only a single function here
    # that needs to be executed
    count_and_say()
