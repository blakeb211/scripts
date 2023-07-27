import ast, traceback
import sys

if sys.argv[1]:
    filename = sys.argv[1] 
else:
    print("No filename argument given.")
    sys.exit(0);
with open(filename) as f:
    source = f.read()
valid = True
try:
    ast.parse(source)
except SyntaxError:
    valid = False
    traceback.print_exc()
if valid:
    print("Good AST")
else:
    print("Bad AST")
