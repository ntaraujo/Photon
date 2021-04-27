file = 'None'
line = 'None'
line_number = 0


class Raise:
    def __init__(self, node, error, msg):
        import sys
        sys.tracebacklimit = 0

        where = f'File "{file}", line {line_number}, node {node.id}:'
        index = " " * line.index(node.line_slice) + '^'

        msg = f'\n{where}\n\t{line}\n\t{index}\n\t{msg}\n'
        raise error(msg)


class InternalRaise:
    def __init__(self, error, msg):
        import sys
        sys.tracebacklimit = 1000
        raise error(msg)
