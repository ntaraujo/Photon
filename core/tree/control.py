file = 'None'
line = 'None'
line_slice = 'None'
line_number = 0
node_id = 0


class Raise:
    def __init__(self, error, msg):
        where = f'File "{file}", line {line_number}, node {node_id}:'
        index = " " * line.index(line_slice) + '^'

        msg = f'\n{where}\n\t{line}\n\t{index}\n\t{msg}\n'

        import sys
        sys.tracebacklimit = 0
        raise error(msg)
