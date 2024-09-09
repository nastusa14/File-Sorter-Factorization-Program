# File Sorter by Extension
Overview

This Python script sorts files from a source directory into a destination directory based on their file extensions. The program is designed to handle large directories with multiple subdirectories by utilizing multithreading to improve performance.

How It Works

Directory Traversal:

The script recursively traverses through the specified source directory and all its subdirectories using os.walk().

Sorting Files by Extension:

As it encounters files, the program extracts each file's extension and determines the corresponding destination subdirectory based on that extension. For example, all .jpg files will be moved to a jpg/ subdirectory within the destination directory.

Multithreading:

To speed up the file copying process, the program uses the ThreadPoolExecutor from the concurrent.futures module. Each subdirectory is processed in parallel, allowing for faster traversal and file copying.

Creating Directories:

If the destination directory or any of the subdirectories based on the file extensions do not exist, the program will create them automatically.

Command-Line Arguments:

The program accepts two command-line arguments:

source_dir: The path to the source directory that contains the files to be sorted (this is required).

destination_dir: The path to the destination directory where the sorted files will be placed (optional, defaults to a directory named dist).

Usage

python file_sorter.py /path/to/source_directory [options]

Options:

-d, --destination_dir: (Optional) Specify the path to the destination directory. The default is dist.

Example:

python file_sorter.py /home/user/pictures -d /home/user/sorted_files

This command will sort all files from the /home/user/pictures directory into /home/user/sorted_files, creating subdirectories for each file type based on their extensions.
# Factorization Program
This Python program factorizes a list of numbers, returning a list of divisors for each number. It includes both a synchronous version and a parallel version that utilizes multiple CPU cores for faster computation on large numbers.

Key Features:

Synchronous Factorization: The program can calculate the factors of a given number sequentially.

Parallel Factorization: To improve performance, the program can distribute the computation across multiple CPU cores using Python's multiprocessing module. This is useful for handling larger numbers or a large number of inputs more efficiently.

How It Works:

The function factorize_sync(number) finds all the divisors of a single number.

The function factorize_parallel(numbers) distributes the factorization work across multiple CPU cores using a process pool.

The program measures and prints the execution time for both the synchronous and parallel versions to demonstrate performance improvements with parallel processing.

Example Input and Output:

For the input list [128, 255, 99999, 10651060], the program will return:

128: [1, 2, 4, 8, 16, 32, 64, 128]

255: [1, 3, 5, 15, 17, 51, 85, 255]

99999: [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]

10651060: [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

Requirements:

Python 3.6 or higher.
No external libraries are required; the program uses Python's standard multiprocessing module.

How to Run:

Copy the script to a .py file.

Run the script using a terminal or your preferred Python IDE.

The program will execute both synchronous and parallel versions and print the execution times.

Important Note:

To ensure proper parallel execution, the program should be run in a Python script, and the parallel processing logic is enclosed in the if __name__ == '__main__': block.

