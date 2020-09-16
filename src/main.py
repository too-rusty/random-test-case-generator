import random
import os
import default_configs as dc
import time
import generators as genrs
from utils import list_to_str, to_str

# ------------- utils ------------------
generate_non_uniform_random_array = genrs.generate_non_uniform_random_array
generate_uniform_random_array = genrs.generate_uniform_random_array
generate_pairs_non_uniform = genrs.generate_pairs_non_uniform
generate_pairs_uniform = genrs.generate_pairs_uniform
write_to_file = genrs.write_to_file

generate_random_array = genrs.generate_random_array
generate_random_string = genrs.generate_random_string
generate_random_char_matrix = genrs.generate_random_char_matrix
generate_random_tree = genrs.generate_random_tree
generate_random_array_pairs = genrs.generate_random_array_pairs
generate_random_matrix = genrs.generate_random_matrix
generate_random_numbers = genrs.generate_random_numbers
generate_and_write = genrs.generate_and_write

IN_OUT_DIR = os.path.dirname(os.path.abspath(__file__))
IN_OUT_DIR = os.path.join(IN_OUT_DIR, "..", "generated_input")
CODE_DIR = os.path.join(IN_OUT_DIR, "..", "src")


# generates a single input file
# make change here
def generate_custom_input(file_no: int):
    """
    for longest common prefix

    T - 10
    N - 1000, k
    N integers

    """
    tc = random.randint(1, 10)
    content = to_str(tc)  # first line is tc
    for _ in range(tc):
        config = dc.DEFAULT_RANDOM_ARRAY_CONFIG
        # config['str_sizes_uniform_distribution'] = False
        z1 = random.randint(10, 200) if file_no < 8 else 100000
        # z2 = random.randint(10,200) if file_no < 8 else 100000
        config['arr_size_max'] = config['arr_size_min'] = z1
        config['distinct_value_flag'] = random.choice([True, False])
        # k = random.randint(-20,20)
        second_line = list_to_str([z1])
        third_line = generate_random_array(config=config)
        # config['arr_size_max'] = config['arr_size_min'] = z2
        # fourth_line = generate_random_array(config)
        content = list_to_str([content, second_line, third_line], separator="\n")

    return content


def generate_custom_input_strings():
    tc = random.randint(1, 10)
    con = to_str(tc)
    for _ in range(tc):
        config = dc.DEFAULT_RANDOM_STRING_CONFIG
        line1 = generate_random_string(config)
        line2 = generate_random_string(config)
        if random.choice([True, False]):
            line2 = ''
            line2 += line1[0]
            for c in line1[1:]:
                if random.choice([True, False]):
                    line2 += c
        con = list_to_str([con, line2, line1], separator="\n")
    return con


# no changes required here
def generate_n_inputs(st=0, n=10, in_dir=IN_OUT_DIR):
    os.chdir(in_dir)
    _ = [os.remove(f) for f in os.listdir()]  # remove all

    for i in range(st, st + n, 1):
        content = generate_custom_input(i)
        # content = generate_custom_input_strings()
        file_path = os.path.join(in_dir, to_str(i + 1) + ".in")
        write_to_file(file_path, content)


# for python code
def generate_outputs(code_type='python', code_file_name="code.py",
                     in_dir=IN_OUT_DIR, out_dir=IN_OUT_DIR, code_dir=CODE_DIR):
    # call the func on every input file
    # present in the in_dir
    # assumes format to be all test cases
    # else can be modified using config
    # by default same dir
    code_file_path = os.path.join(code_dir, code_file_name)
    os.chdir(in_dir)
    # remove all prev out files
    _ = [os.remove(f) for f in os.listdir() \
         if f.endswith(".out")]

    in_files = [os.path.join(in_dir, f) for f in os.listdir()]
    out_files = [os.path.join(out_dir, f[:-3] + ".out") \
                 for f in os.listdir()]
    exec_code_command = "python "
    if code_type is 'cpp':
        command = 'c++ -std=c++14 ' + code_file_path
        os.system(command)
        exec_code_command = './a.out '

    def gen_out(in_file, out_file):
        read_in_file = "cat " + in_file
        exec_code = exec_code_command + code_file_path
        command = read_in_file + " | " + exec_code + " >> " \
                  + out_file
        os.system(command)

    counter = 0
    for in_file, out_file in zip(in_files, out_files):
        counter += 1
        st = time.time()
        gen_out(in_file, out_file)
        en = time.time()
        print("output generated for ", counter, "in ", (en - st) // 1000)

    if code_type is 'cpp':
        os.system("rm a.out")


def zip_it(problem_id, in_out_dir=IN_OUT_DIR):
    os.chdir(in_out_dir)
    base_dir = os.path.join(in_out_dir, "../")
    file_path = base_dir + "problem_" + to_str(problem_id) + ".zip"
    print(file_path)
    if os.path.exists(file_path):
        rm_command = ["rm", file_path]
        os.system(" ".join(rm_command))
    command = ["zip", file_path, "./{*.in,*.out}"]
    os.system(" ".join(command))


if __name__ == '__main__':
    # can specify st as generate_n_inputs(st=2,n=10)
    # generates 10 tcs from no.2 and
    # the first test case can be input manually
    generate_n_inputs(n=10)
    generate_outputs(code_type='cpp', code_file_name="code.cpp")
    zip_it(1052)

    """
    steps
    1. write code in code.py and call the function 
        inside if __name__ == ....
        NOTE: write function like reading from actual 
            std input and also test it ...
    2. generate inputs, write the code inside generate_inputs
        function
    3. run the current file
        python main.py 
    """
