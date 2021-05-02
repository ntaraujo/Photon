from re import match, IGNORECASE


ignore = r'[\t ]*'
at_start = r'^{}'.format

string_prefix = '|r|b|f|rf|fr|u|rb|br'  # with re.IGNORECASE flag
# string_prefix = r'|[rR]|[bB]|[fF]|[rR][fF]|[fF][rR]|[uU]|[rR][bB]|[bB][rR]'  # 0 = prefix
string_quote = r'"""|\'|"|\'\'\''  # 0 = quote


def not_in(start, end):
    fmt = r'(?!{})'
    if isinstance(start, str):
        return fmt.format(fr'[^{start}]*{end}')  # (?![^\(]*\))
    else:
        fmt = fmt.format('(?:{})')
        return fmt.format('|'.join(fr'[^{start}]*{end}' for start, end in zip(start, end)))  # (?!(?:[^\(]*\)|[^\[]*\]))


def i_match(pattern, _string):
    return match(pattern, _string, IGNORECASE)


rest = fr'{ignore}(.*)'  # 1 = rest
indent = fr'^({ignore})(.*)'  # 1 = indent, 2 = line

# 1 = prefix, 2 = quote, 3 = content, 4 = rest
string_everywhere = fr'({string_prefix})({string_quote})(((?!\2).*)\2){rest}'
string = at_start(string_everywhere)
# BR'''Brazil'''

# 1 = integer, 2 = rest
integer_everywhere = fr'(0o[0-9]+|[^0][0-9]+|[0-9]){rest}'
integer = at_start(integer_everywhere)
# 0o25

# 1 = var, 2 = rest
var_everywhere = fr'([a-zA-Z_]+[0-9a-zA-Z_]*){rest}'
var = at_start(var_everywhere)
# var_name1

# 1 = arguments
call_everywhere = fr'\({ignore}(.*){ignore}\){ignore}$'
call = at_start(call_everywhere)
# (argument1, argument2)

containers_start_end = (r'\[', r'\(', r'\{'), (r'\]', r'\)', r'\}')
comma_not_in_container = fr',{not_in(*containers_start_end)}'
# [0, 1], {0:1, 2:3}
#   x   ^     x

quote = r'\'', r'\"', r'"""', r'\'\'\''
hashtag_not_in_quotes = fr'#{not_in(quote, quote)}'
# "hashtag is #"  # explanation
#             x   ^

# 1 = key, 2 = value, 3 = rest
mapping_everywhere = fr'(.*){ignore}[:=]{ignore}(.*)(?:{comma_not_in_container})?{rest}'
mapping = at_start(mapping_everywhere)
# a:b,

# 1 = arg, 2 = rest
arg_everywhere = fr'(.*){ignore}(?:{comma_not_in_container})?{rest}'
arg = at_start(arg_everywhere)
# a,

# 0 = comment
comment = fr'{hashtag_not_in_quotes}.*$'

# 1 = var, 2 = value|rest
set_var_everywhere = fr'({var_everywhere}){ignore}={rest}'
set_var = at_start(set_var_everywhere)
# var_name2 = ...

# 1 = attr, 2 = rest
attr_everywhere = fr'\.({var_everywhere}){rest}'
attr = at_start(attr_everywhere)
# .var_name3


def check(self):
    check = match(self.regex, self.line_slice)
    if check is None:
        return
    else:
        self.var = check[0]
        return check[1]
