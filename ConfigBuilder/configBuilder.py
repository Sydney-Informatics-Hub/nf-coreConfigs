#!/usr/bin/env python3

def ask_for_input(prompt, type_=None, min_=None, max_=None, num_of_attempts=3):
    for _ in range(num_of_attempts):
        val = input(prompt)
        if type_ is not None:
            try:
                val = type_(val)
            except ValueError:
                print(f"Input type must be {type_.__name__}!")
                continue
        if min_ is not None and val < min_:
            print(f"Input must be greater than or equal to {min_}!")
        elif max_ is not None and val > max_:
            print(f"Input must be less than or equal to {max_}!")
        else:
            return val
    raise ValueError('Invalid Input')

def main():
    executor = input("What executor does your system use (default is 'local')? ")
    executor = executor if executor else 'local'

    queue = None
    if executor in ['pbspro', 'slurm', 'azure batch', 'aws batch', 'bridge', 'flux', 'lsf', 'moab', 'oar', 'nqsii', 'pbs', 'sge']:
        queue = input("What queue would you like to run your jobs on? ")
    
    cpus = ask_for_input("What is the max number of CPUs available on this queue (default is 1)? ", type_=int, min_=1)
    cpus = cpus if cpus else 1

    memory = ask_for_input("What is the max amount of memory in GB available on this queue (default is 1)? ", type_=int, min_=1)
    memory = memory if memory else 1
    
    output_file = input("Enter the output file name (default is 'nextflow.config'): ")
    output_file = output_file if output_file else 'custom_nextflow.config'

    with open(output_file, 'w') as f:
        f.write("// Custom Nextflow config file \n\n")
        f.write("process {\n")
        f.write(f"    executor = '{executor}'\n")
        if queue:
            f.write(f"    queue = '{queue}'\n")
        f.write(f"    cpus = {cpus}\n")
        f.write(f"    memory = '{memory} GB'\n")
        f.write("}")

if __name__ == '__main__':
    main()
