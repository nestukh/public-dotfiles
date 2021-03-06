from __future__ import print_function

import subprocess

pythons = subprocess.check_output(['eselect', '--brief', 'python', 'list'])
pythons = [python.replace('.', '_') for python in pythons.splitlines()]
assert len(pythons)

python = subprocess.check_output(['eselect', '--brief', 'python', 'show'])
python = python.replace('.', '_').strip()
assert python

py2 = subprocess.Popen(
    ['eselect', '--brief', 'python', 'show', '--ABI', '--python2'],
    stdout=subprocess.PIPE).communicate()[0].strip()
py3 = subprocess.Popen(
    ['eselect', '--brief', 'python', 'show', '--ABI', '--python3'],
    stdout=subprocess.PIPE).communicate()[0].strip()
assert len(py2) and len(py3)

if __name__ == "__main__":
    print(pythons)
    print(python)
    print(py2, py3)
    exit()


text("""# $warning
PYTHON_TARGETS="$pythons"
PYTHON_SINGLE_TARGET="$python"
USE_PYTHON="$py2 $py3"
""").render(pythons=" ".join(pythons), py2=py2, py3=py3, python=python)
