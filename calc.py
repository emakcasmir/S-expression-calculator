import sys
import re

def assess_expression(expr):
    # Match integer literals
    if re.match(r'^\d+$', expr):
        return int(expr)

    # Match addition expressions
    match = re.match(r'^\(add (\d+) (\d+)\)$', expr)
    if match:
        return int(match.group(1)) + int(match.group(2))

    # Match multiplication expressions
    match = re.match(r'^\(multiply (\d+) (\d+)\)$', expr)
    if match:
        return int(match.group(1)) * int(match.group(2))

    raise ValueError('Invalid expression')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} <expression>'.format(sys.argv[0]))
        sys.exit(1)

    try:
        result = assess_expression(sys.argv[1])
        print(result)
    except ValueError as e:
        print(str(e))
        sys.exit(1)
