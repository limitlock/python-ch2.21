s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

S = s.upper()
arr = S.replace(',', ' ').replace('.',' ').replace('\n', ' ').split()
arr.sort(key=str)
for i in arr:
    print(i+' : ')