import os.path
from typing import List


def readInput(day) -> List[str]:
    with open(os.path.join('inputs', day + '.txt'), 'r') as f:
        return f.read().splitlines()
