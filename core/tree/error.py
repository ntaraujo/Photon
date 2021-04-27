file = 'None'
line = 'None'
line_number = 0


class Raise:
    def __init__(self, node, error, msg):
        where = f'File "{file}", line {line_number}, node {node.id}:'
        index = " " * line.index(node.line_slice) + '^'

        msg = f'\n{where}\n\t{line}\n\t{index}\n\t{msg}\n'

        import sys
        sys.tracebacklimit = 0
        raise error(msg)
