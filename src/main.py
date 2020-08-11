import random
import os
from numpy import random as npr


# ------------- utils ------------------
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


def write_to_file(file_path, content):
    try:
        file = open(file_path, 'w')
        file.write(content)
        file.close()
    except Exception as e:
        print(e)
        # todo maybe better error handling
        print('error in writing to file')


# ----------- main functions -------------------------
def generate_random_array(file_path, config={}):
    def gen_arr_str(N, min_v, max_v, distinct, include_n):
        res = generate_uniform_random_array(N, min_v, max_v) if distinct \
            else generate_non_uniform_random_array(N, min_v, max_v)
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
        Ns = (generate_non_uniform_random_array(tc, N_min, N_max) if not N_uniform \
                  else generate_uniform_random_array(tc, N_min, N_max)) if not N_same \
            else generate_non_uniform_random_array(tc, N_min, N_min)
        res = [gen_arr_str(N, min_val, max_val, distinct_val, include_n) for N in Ns]
        # todo shuffle res
        if include_tc:
            res.append(tc.__str__())
            res.reverse()
        content = "\n".join(res)
        write_to_file(file_path, content)
        return True
    except Exception as e:
        print(e)
        return False


def generate_random_string(file_path, config={}):
    try:
        tc = config['n_test_cases']
        include_tc = config['include_n_test_cases_flag']
        include_n = config['include_n_flag']
        N_min = config['str_size_min']
        N_max = config['str_size_max']
        N_same = config['str_sizes_all_same']
        N_uniform = config['str_sizes_uniform_distribution']
        chars = config['chars']
        pass

        return  True
    except Exception as e:
        print(e)
        return  False



def generate_random_char_matrix(file_path, config={}):
    pass


def generate_random_array_pairs(file_path, config={}):
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
        Ns = (generate_non_uniform_random_array(tc, N_min, N_max) if not N_uniform \
                  else generate_uniform_random_array(tc, N_min, N_max)) if not N_same \
            else generate_non_uniform_random_array(tc, N_min, N_min)
        res = [gen_pairs_str(N, min_first, max_first, min_second, max_second, order, include_n) for N in Ns]
        if include_tc:
            res.append(tc.__str__())
            res.reverse()
        content = "\n".join(res)
        write_to_file(file_path, content)
        return True
    except Exception as e:
        print(e)
        return False


def generate_random_matrix(file_path, config={}):
    # todo make different rows and columns
    def gen_matrix(r, c, min_v, max_v, distinct):
        return list(generate_uniform_random_array(r * c, min_v, max_v) if distinct \
                        else generate_non_uniform_random_array(r * c, min_v, max_v))

    def make_mat_str(rows, cols, arr, include_nm):
        assert len(arr) == rows * cols
        res = [" ".join(map(lambda x: x.__str__(), arr[i * cols: (i + 1) * cols])) for i in range(rows)]
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
        write_to_file(file_path, "\n".join(mat))
        return True

    except Exception as e:
        print(e)
        return False


def generate_random_numbers(file_path, config={}):
    try:
        n_test_cases = config['n_test_cases']
        min_val = config['min_value']
        max_val = config['max_value']
        include_n = config['include_n_test_cases_flag']
        uniform = config['distinct_value_flag']
        nums = generate_uniform_random_array(n_test_cases, min_val, max_val) if uniform \
            else generate_non_uniform_random_array(n_test_cases, min_val, max_val)
        nums = list(nums)
        # todo shuffle
        if include_n:
            nums.append(n_test_cases)
            nums.reverse()
        content = "\n".join(map(lambda x: x.__str__(), nums))
        write_to_file(file_path, content)
        return True
    except Exception as e:
        print(e)
        return False


# ---------- for manual test case generation ----------

def write_list(file_path, list, include_tc=True, include_n=True):
    pass


def write_list_of_list(file_path, list_of_list, include_tc=True, include_n=True):
    pass


def main():
    parent_dir = os.path.join(os.getcwd(), "..", "generated_input")
    generate_random_numbers(os.path.join(parent_dir, 'a.in'), config={
        'n_test_cases': 10,
        'min_value': 1,
        'max_value': 1,
        'include_n_test_cases_flag': True,
        'distinct_value_flag': True
    })
    generate_random_array(os.path.join(parent_dir, 'b.in'), config={
        'n_test_cases': 10,
        'arr_size_min': 1,
        'arr_size_max': 1,  # dont care if next true
        'arr_sizes_all_same': False,
        'arr_sizes_uniform_distribution': False,  # dont care if prev true
        'min_value': 2,
        'max_value': 10,
        'distinct_value_flag': True,
        'include_n_flag': True,
        'include_n_test_cases_flag': True,
    })
    generate_random_array_pairs(os.path.join(parent_dir, 'c.in'), config={
        'n_test_cases': 10,
        'arr_size_min': 1,
        'arr_size_max': 5,  # dont care if next true
        'arr_sizes_all_same': False,
        'arr_sizes_uniform_distribution': True,  # dont care if prev true
        'min_first_value': 2,
        'max_first_value': 10,
        'min_second_value': 2,
        'max_second_value': 12,  # if inc then > max_first_val and so on
        'a_b_order': 'inc',
        'include_n_flag': True,
        'include_n_test_cases_flag': True,
    })
    generate_random_matrix(os.path.join(parent_dir, 'd.in'), config={
        'n_test_cases': 10,
        'include_n_test_cases_flag': True,
        'num_rows_min': 1,
        'num_rows_max': 4,
        'num_cols_min': 1,
        'num_cols_max': 4,
        'arr_sizes_all_same': True,  # true if all n ,m are same
        'arr_sizes_uniform_distribution': False,
        'min_value': 1,
        'max_value': 10,
        'distinct_flag': True,
        'include_n_m_flag': True,
        'square': True
    })


if __name__ == '__main__':
    main()
