import os
import shutil
import argparse
from concurrent.futures import ThreadPoolExecutor

def copy_file(src_file, dst_dir):
    try:
        shutil.copy(src_file, dst_dir)
    except Exception as e:
        print(f"Error copying {src_file}: {e}")

def process_directory(src_dir, dst_base_dir):
    for root, _, files in os.walk(src_dir):
        for file in files:
            src_file = os.path.join(root, file)
            extension = os.path.splitext(file)[1][1:]
            dst_dir = os.path.join(dst_base_dir, extension)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            copy_file(src_file, dst_dir)

def main():
    parser = argparse.ArgumentParser(description="Sort files in a directory by extension.")
    parser.add_argument("source_dir", help="Path to the source directory.")
    parser.add_argument("-d", "--destination_dir", default="dist", help="Path to the destination directory. Default is 'dist'.")
    args = parser.parse_args()

    source_dir = args.source_dir
    destination_dir = args.destination_dir

    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    with ThreadPoolExecutor() as executor:
        futures = []
        for root, dirs, _ in os.walk(source_dir):
            for dir in dirs:
                src_sub_dir = os.path.join(root, dir)
                futures.append(executor.submit(process_directory, src_sub_dir, destination_dir))
        
        for future in futures:
            future.result()

if __name__ == "__main__":
    main()