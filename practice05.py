s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

S = s.upper()
arr = S.replace(',', ' ').replace('.',' ').replace('\n', ' ').split()
arr = list(set(arr))
print(arr)
for i in arr:
    print('{0}:{1}'.format(i, arr.count(i)))