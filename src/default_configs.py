DEFAULT_RANDOM_NUMBERS_CONFIG = {
    'n_test_cases': 10,
    'min_value': 1,
    'max_value': 1,
    'include_n_test_cases_flag': False,
    'distinct_value_flag': False
}
DEFAULT_RANDOM_ARRAY_CONFIG = {
    'n_test_cases': 1,
    'arr_size_min': 1,
    'arr_size_max': 100,  # dont care if next true
    'arr_sizes_all_same': False,
    'arr_sizes_uniform_distribution': False,  # dont care if prev true
    'min_value': 1,
    'max_value': 200,
    'distinct_value_flag': True,
    'include_n_flag': False,
    'include_n_test_cases_flag': False,
}
DEFAULT_RANDOM_ARRAY_PAIRS_CONFIG = {
    'n_test_cases': 10,
    'arr_size_min': 1,
    'arr_size_max': 5,  # dont care if next true
    'arr_sizes_all_same': False,
    'arr_sizes_uniform_distribution': True,  # dont care if prev true
    'min_first_value': 2,
    'max_first_value': 10,
    'min_second_value': 2,
    'max_second_value': 12,
    'a_b_order': 'rand',  # if inc then > max_first_val and so on
    'include_n_flag': False,
    'include_n_test_cases_flag': False,
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
    'num_rows_min': 2,
    'num_rows_max': 5,
    'num_cols_min': 3,
    'num_cols_max': 7,
    'arr_sizes_all_same': False,
    'arr_sizes_uniform_distribution': True,
    'chars': "abcdsdasljd",
    'distinct_flag': False,
    'include_n_m_flag': True,
    'square': False,
}

DEFAULT_RANDOM_STRING_CONFIG = {
    'n_test_cases': 1,
    'include_n_test_cases_flag': False,
    'include_n_flag': False,
    'str_size_min': 1,
    'str_size_max': 100,
    'str_sizes_all_same': False,
    'str_sizes_uniform_distribution': True,
    'chars': "abcdefghijklmnopqrstuvwxyz",
    'distinct_chars_flag': True,
}

if __name__ == '__main__':
    pass
