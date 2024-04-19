# To print a list of targets available to you

import cudaq

targets = cudaq.get_targets()

for t in targets:
    print(t)
