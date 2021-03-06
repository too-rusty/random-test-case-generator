import random
from utils import list_to_str, to_str

def generate_non_uniform_random_array(N, min_val, max_val):
    for _ in range(N):
        yield random.randint(min_val, max_val)

def generate_uniform_random_array(N, min_val, max_val):
    res = []
    if max_val - min_val + 1 >= N:
        # n is smaller compared to range so generate distinct
        # divide into buckets and choose randomly from each
        extra = (max_val - min_val + 1) % N
        bucket_size = (max_val - min_val + 1) // N
        st = 0
        for i in range(N - 1):
            offset = 1 if i < extra else 0
            lo, hi = min_val + st, min_val + st + offset + bucket_size - 1
            yield random.randint(lo, hi)
            st += bucket_size + offset
        yield random.randint(min_val + st, max_val)
    else:
        # n is much larger hence include everything with uniform distribution
        for i in range(N):
            yield min_val + i % (max_val - min_val + 1)


def generate_pairs_non_uniform(N, p0min, p0max, p1min, p1max):
    # order is random and everything is random
    gen1 = iter(generate_non_uniform_random_array(N, p0min, p0max))
    gen2 = iter(generate_non_uniform_random_array(N, p1min, p1max))
    for _ in range(N):
        yield (next(gen1), next(gen2))

def generate_pairs_uniform(N, p0min, p0max, p1min, p1max, order):
    # order is inc, dec, noninc, nondec
    if not order in ['inc', 'dec', 'noninc', 'nondec']:
        raise Exception("order invalid")
    gen = iter(generate_uniform_random_array(N, p0min, p0max))
    for _ in range(N):
        first = next(gen)
        if order is 'inc':
            yield (first, random.randint(first + 1, min(p1max, max(first + 1, p1max))))
        elif order == 'dec':
            yield (first, random.randint(max(p1min, min(p1min, first - 1)), first - 1))
        elif order is 'noninc':
            yield (first, random.randint(max(p1min, min(p1min, first)), first))
        elif order is 'nondec':
            yield (first, random.randint(first, min(p1max, max(first + 1, p1max))))

def write_to_file(file_path: str, content: str):
    try:
        file = open(file_path, 'w')
        file.write(content)
        file.close()
    except Exception as e:
        print(e)
        # todo maybe better error handling
        print('error in writing to file')



# ----------- main functions -------------------------
def generate_random_array(config={},fns=[]):
    def gen_arr_str(N, min_v, max_v, distinct, include_n):
        res = generate_uniform_random_array(N, min_v, max_v) if distinct \
            else generate_non_uniform_random_array(N, min_v, max_v)
        res = list(res)
        for fn in fns:
            res = fn(res)
        res = map(lambda x: x.__str__(), res)
        res = [" ".join(res)]
        if include_n:
            res.append(N.__str__())
            res.reverse()
        return "\n".join(res)

    try:
        tc = config['n_test_cases']
        N_min = config['arr_size_min']
        N_max = config['arr_size_max']
        N_same = config['arr_sizes_all_same']
        N_uniform = config['arr_sizes_uniform_distribution']
        min_val = config['min_value']
        max_val = config['max_value']
        distinct_val = config['distinct_value_flag']
        include_n = config['include_n_flag']
        include_tc = config['include_n_test_cases_flag']
    except Exception as e:
        print(e)
        return None
    Ns = (generate_non_uniform_random_array(tc, N_min, N_max) if not N_uniform \
              else generate_uniform_random_array(tc, N_min, N_max)) if not N_same \
        else generate_non_uniform_random_array(tc, N_min, N_min)
    res = [gen_arr_str(N, min_val, max_val, distinct_val, include_n) for N in Ns]
    # todo shuffle res
    if include_tc:
        res.append(tc.__str__())
        res.reverse()
    content = "\n".join(res)
    return content


def generate_random_string(config={}):
    def get_str(chars, N, distinct, include_n):
        res = "".join([random.choice(chars) for _ in range(N)])
        if distinct:
            res = "".join(chars[i % len(chars)] for i in range(N))
            # todo shuffle
        res = N.__str__() + "\n" + res if include_n else res
        return res

    try:
        tc = config['n_test_cases']
        include_tc = config['include_n_test_cases_flag']
        include_n = config['include_n_flag']
        N_min = config['str_size_min']
        N_max = config['str_size_max']
        N_same = config['str_sizes_all_same']
        N_uniform = config['str_sizes_uniform_distribution']
        chars = config['chars']
        distinct = config['distinct_chars_flag']
    except Exception as e:
        print(e)
        return None
    Ns = (generate_non_uniform_random_array(tc, N_min, N_max) if not N_uniform \
              else generate_uniform_random_array(tc, N_min, N_max)) if not N_same \
        else generate_non_uniform_random_array(tc, N_min, N_min)
    res = [get_str(chars, N, distinct, include_n) for N in Ns]
    if include_tc:
        res.append(tc.__str__())
        res.reverse()
    content = "\n".join(res)
    return content


def generate_random_char_matrix(config={}):
    def gen_string(r, c, chars, distinct):
        res = "".join([random.choice(chars) for _ in range(r * c)])
        if distinct:
            res = "".join(chars[i % len(chars)] for i in range(r * c))
        return res

    def make_mat_str(rows, cols, string, include_nm, delim=""):
        assert len(string) == rows * cols
        res = [delim.join(map(lambda x: x.__str__(), string[i * cols: (i + 1) * cols])) \
               for i in range(rows)]
        if include_nm:
            res.append(rows.__str__() + " " + cols.__str__())
            res.reverse()
        return "\n".join(res)

    try:
        tc = config['n_test_cases']
        include_tc = config['include_n_test_cases_flag']
        rows_min = config['num_rows_min']
        rows_max = config['num_rows_max']
        cols_min = config['num_cols_min']
        cols_max = config['num_cols_max']
        N_same = config['arr_sizes_all_same']
        N_uniform = config['arr_sizes_uniform_distribution']
        chars = config['chars']
        distinct = config['distinct_flag']
        include_nm = config['include_n_m_flag']
        square = config['square']
    except Exception as e:
        print(e)
        return None
    if square:
        Ns = list(generate_uniform_random_array(tc, rows_min, rows_max) if N_uniform \
                      else generate_non_uniform_random_array(tc, rows_min, rows_max))
        NMs = zip(Ns, Ns)
    else:
        Ns = list(generate_uniform_random_array(tc, rows_min, rows_max) if N_uniform \
                      else generate_non_uniform_random_array(tc, rows_min, rows_max))
        Ms = generate_non_uniform_random_array(tc, cols_min, cols_max)
        NMs = zip(Ns, Ms)
    NMs = list(NMs)
    NMs = [NMs[0] for _ in range(tc)] if N_same else NMs
    mat = [make_mat_str(r, c, gen_string(r, c, chars, distinct), include_nm) \
           for r, c in NMs]
    if include_tc:
        mat.append(tc.__str__())
        mat.reverse()
    content = "\n".join(mat)
    return content


def generate_random_tree(nodes, show_edges=True):
    content = []
    arr = [i for i in range(nodes)]
    random.shuffle(arr)
    edges = []
    parent = [-1 for _ in range(nodes)]
    for idx, v in enumerate(arr):
        if not idx is 0:
            parent[v] = random.choice(arr[:idx])
            edges.append((parent[v] + 1, v + 1))
    content.append(to_str(nodes))
    if show_edges:
        content.append(list_to_str(map(lambda l: list_to_str(l), edges), "\n"))
    else:
        content.append(list_to_str(parent))
    content = list_to_str(content, "\n")
    # the one with -1 is the root

    return content


global tim


def dfs(u, pr, G, st, en):
    global tim
    st[u] = tim
    tim += 1
    # print("vis ", u, "st ", st[u])
    for v in G[u]:
        if v == pr: continue
        dfs(v, u, G, st, en)
    # tim+=1
    # print("end ", u, "en ", tim)
    en[u] = tim
    tim += 1


# this function is for a custom test case
# to gen in and out ordering from the tree
def generate_ordering_from_tree(nodes, correct_ordering=True):
    global tim
    tim = 1
    # sten = None
    if nodes is 1:
        sten = [(1, 2)] if correct_ordering \
            else [(random.randint(1, 10), random.randint(1, 10))]
    else:
        input = generate_random_tree(nodes)
        edges = list(map(lambda x: tuple(map(int, x.split(" "))), input.split("\n")[1:]))
        # print(nodes, edges)
        st = [-1 for _ in range(nodes)]
        en = [-1 for _ in range(nodes)]
        G = [[] for _ in range(nodes)]
        for e in edges:
            u, v = map(lambda x: x - 1, e)
            G[u].append(v)
            G[v].append(u)
        dfs(0, -1, G, st, en)
        sten = list(zip(st, en))

        def modify(tup, lis_tup, after, type):
            if type == "overlap":
                x, y = random.choice(lis_tup[after:])
                return (random.randint(x, y), random.randint(y, y + 10))
            if type == "inc":
                x, y = tup
                lim = random.randint(0, 10)
                return (x + random.randint(0, lim), y + random.randint(0, lim))
            if type == "eq":
                return random.choice(lis_tup[after:])

        if not correct_ordering:
            # modify sten to be incorrect
            to_mod = random.randint(1, nodes - 1)
            for i in range(to_mod):
                sten[i] = modify(sten[i], sten,
                                 to_mod, random.choice(["eq", "inc", "overlap"]))
    # print(sten)
    content = to_str(nodes)
    content = [content, list_to_str(map(lambda l: list_to_str(l), sten), "\n")]
    content = list_to_str(content, "\n")
    return content


def test2():
    # c = generate_random_tree(5, show_edges=False)
    # print(c)
    print(generate_ordering_from_tree(10))


def generate_random_array_pairs(config={}):
    # for inc dec the ranges must be valid
    # need to figure out for distinct or maybe not needed
    def gen_pairs_str(N, min0, max0, min1, max1, order, include_n):
        if order is 'rand':
            tmp = generate_pairs_non_uniform(N, min0, max0, min1, max1)
        else:
            tmp = generate_pairs_uniform(N, min0, max0, min1, max1, order)
        # print(tmp)
        tmp = ["\n".join(map(lambda tup: tup[0].__str__() + " " + tup[1].__str__(), tmp))]
        if include_n:
            tmp.append(N.__str__())
            tmp.reverse()
        return "\n".join(tmp)

    try:
        tc = config['n_test_cases']
        N_min = config['arr_size_min']
        N_max = config['arr_size_max']
        N_same = config['arr_sizes_all_same']
        N_uniform = config['arr_sizes_uniform_distribution']
        min_first = config['min_first_value']
        max_first = config['max_first_value']
        min_second = config['min_second_value']
        max_second = config['max_second_value']
        order = config['a_b_order']
        include_n = config['include_n_flag']
        include_tc = config['include_n_test_cases_flag']
    except Exception as e:
        print(e)
        return None
    Ns = (generate_non_uniform_random_array(tc, N_min, N_max) if not N_uniform \
              else generate_uniform_random_array(tc, N_min, N_max)) if not N_same \
        else generate_non_uniform_random_array(tc, N_min, N_min)
    res = [gen_pairs_str(N, min_first, max_first, min_second, max_second, order, include_n) \
           for N in Ns]
    if include_tc:
        res.append(tc.__str__())
        res.reverse()
    content = "\n".join(res)
    # write_to_file(file_path, content)
    return content

def generate_random_matrix(config={}):
    # todo make different rows and columns
    def gen_matrix(r, c, min_v, max_v, distinct):
        return list(generate_uniform_random_array(r * c, min_v, max_v) if distinct \
                        else generate_non_uniform_random_array(r * c, min_v, max_v))

    def make_mat_str(rows, cols, arr, include_nm):
        assert len(arr) == rows * cols
        res = [" ".join(map(lambda x: x.__str__(), arr[i * cols: (i + 1) * cols])) \
               for i in range(rows)]
        if include_nm:
            res.append(rows.__str__() + " " + cols.__str__())
            res.reverse()
        return "\n".join(res)

    try:
        tc = config['n_test_cases']
        include_tc = config['include_n_test_cases_flag']
        rows_min = config['num_rows_min']
        rows_max = config['num_rows_max']
        cols_min = config['num_cols_min']
        cols_max = config['num_cols_max']
        N_same = config['arr_sizes_all_same']
        N_uniform = config['arr_sizes_uniform_distribution']
        min_val = config['min_value']
        max_val = config['max_value']
        distinct = config['distinct_flag']
        include_nm = config['include_n_m_flag']
        square = config['square']
    except Exception as e:
        print(e)
        return None
    if square:
        Ns = list(generate_uniform_random_array(tc, rows_min, rows_max) if N_uniform \
                      else generate_non_uniform_random_array(tc, rows_min, rows_max))
        NMs = zip(Ns, Ns)
    else:
        Ns = list(generate_uniform_random_array(tc, rows_min, rows_max) if N_uniform \
                      else generate_non_uniform_random_array(tc, rows_min, rows_max))
        Ms = generate_non_uniform_random_array(tc, cols_min, cols_max)
        NMs = zip(Ns, Ms)
    NMs = list(NMs)
    NMs = [NMs[0] for _ in range(tc)] if N_same else NMs
    mat = [make_mat_str(r, c, gen_matrix(r, c, min_val, max_val, distinct), include_nm) \
           for r, c in NMs]
    if include_tc:
        mat.append(tc.__str__())
        mat.reverse()
    # write_to_file(file_path, "\n".join(mat))
    return "\n".join(mat)


def generate_random_numbers(config={}):
    try:
        n_test_cases = config['n_test_cases']
        min_val = config['min_value']
        max_val = config['max_value']
        include_n = config['include_n_test_cases_flag']
        uniform = config['distinct_value_flag']
    except Exception as e:
        print(e)
        return None
    nums = generate_uniform_random_array(n_test_cases, min_val, max_val) if uniform \
        else generate_non_uniform_random_array(n_test_cases, min_val, max_val)
    nums = list(nums)
    # todo shuffle
    if include_n:
        nums.append(n_test_cases)
        nums.reverse()
    content = "\n".join(map(lambda x: x.__str__(), nums))

    return content


def generate_and_write(func, config):
    def write(file_path):
        content = func(config)
        if content is None: return False
        write_to_file(file_path, content)
        return True

    return write




