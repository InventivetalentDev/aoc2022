import os
import shutil

from util import readInput

inp = readInput('day7')


# based on https://stackoverflow.com/a/1392549/6257838
def get_size(start_path='.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                with open(fp, 'r') as f:
                    total_size += int(f.read())

    return total_size


path = []

filesystem_size = 70000000
required_size = 30000000

max_size = 100000
summed_size = 0
total_size = 0

root = './tmp/day7'

# cleanup first
shutil.rmtree(root)

last_dir_name = ''
current_dir_name = '/'
current_contents = []
expect_ls = False
for line in inp:
    print(line)
    if line.startswith("$"):
        cmd, *args = line[2:].split(' ')
        match cmd:
            case 'cd':
                expect_ls = False

                if args[0] == "..":

                    dirpath = os.path.join(root, *path[1:])
                    size = get_size(dirpath)

                    if size < max_size:
                        summed_size += size

                    total_size += size

                    # go one up
                    path.pop()
                    current_dir_name = last_dir_name
                else:
                    path.append(args[0])
                    last_dir_name = current_dir_name
                    current_dir_name = args[0]

                # print(">", current_dir_name)
            case 'ls':
                expect_ls = True
        continue

    if expect_ls:
        meta, file = line.split(' ')
        current_contents.append(line)

        filepath = os.path.join(root, *path[1:], file)
        print(filepath)

        if meta == 'dir':
            # print("> mkdir", filepath)
            os.makedirs(filepath, exist_ok=True)
        else:
            # print("> write", filepath)
            with open(filepath, 'w') as f:
                f.write(meta)

root_size = get_size(root)

print(summed_size)
print("root", root_size)
unused = filesystem_size - root_size
print("unused", unused)
to_delete = required_size - unused
print("need to delete", to_delete)

smallest = filesystem_size
for dirpath, dirnames, filenames in os.walk(root):
    for d in dirnames:
        print(d)
        path = os.path.join(dirpath, d)
        print(path)
        sze = get_size(path)
        print(sze)
        if sze >= to_delete and sze < smallest:
            smallest = sze

print(smallest)
