DEFAULT_RANDOM_NUMBERS_CONFIG = {
    'n_test_cases': 5,
    'min_value': 1,
    'max_value': 7,
    'include_n_test_cases_flag': True,
    'distinct_value_flag': True
}
DEFAULT_RANDOM_ARRAY_CONFIG = {
    'n_test_cases': 1,
    'arr_size_min': 1,
    'arr_size_max': 1000,  # dont care if next true
    'arr_sizes_all_same': False,
    'arr_sizes_uniform_distribution': False,  # dont care if prev true
    'min_value': 1,
    'max_value': 100,
    'distinct_value_flag': False,
    'include_n_flag': False,
    'include_n_test_cases_flag': False,
}
DEFAULT_RANDOM_ARRAY_PAIRS_CONFIG = {
    'n_test_cases': 10,
    'arr_size_min': 1,
    'arr_size_max': 100000,  # dont care if next true
    'arr_sizes_all_same': False,
    'arr_sizes_uniform_distribution': False,  # dont care if prev true
    'min_first_value': 1,
    'max_first_value': 90000,
    'min_second_value': 1,
    'max_second_value': 100000,
    'a_b_order': 'inc',  # if inc then > max_first_val and so on
    'include_n_flag': True,
    'include_n_test_cases_flag': True,
}
DEFAULT_RANDOM_MATRIX_CONFIG = {
    'n_test_cases': 10,
    'include_n_test_cases_flag': False,
    'num_rows_min': 1,
    'num_rows_max': 4,
    'num_cols_min': 1,
    'num_cols_max': 4,
    'arr_sizes_all_same': True,  # true if all n ,m are same
    'arr_sizes_uniform_distribution': False,
    'min_value': 1,
    'max_value': 10,
    'distinct_flag': True,
    'include_n_m_flag': False,
    'square': True
}

DEFAULT_RANDOM_CHAR_MATRIX_CONFIG = config = {
    'n_test_cases': 10,
    'include_n_test_cases_flag': True,
    'num_rows_min': 1,
    'num_rows_max': 1000,
    'num_cols_min': 1,
    'num_cols_max': 1000,
    'arr_sizes_all_same': False,
    'arr_sizes_uniform_distribution': True,
    'chars': "OX",
    'distinct_flag': False,
    'include_n_m_flag': True,
    'square': False,
}

DEFAULT_RANDOM_STRING_CONFIG = {
    'n_test_cases': 1,
    'include_n_test_cases_flag': False,
    'include_n_flag': False,
    'str_size_min': 1,
    'str_size_max': 10000,
    'str_sizes_all_same': False,
    'str_sizes_uniform_distribution': True,
    'chars': "ABCDEFGHIJKLMNOPQRSTUBWXYZ".lower(),
    'distinct_chars_flag': False,
}

if __name__ == '__main__':
    pass
