patterns = {
  ('hashtag',): comment,
  ('singleQuote',): string,
  ('doubleQuote',): string,
  ('type', 'beginBlock', 'num'): arrayType,
  ('var', 'beginBlock', 'num'): arrayType,
  ('type', 'beginBlock', 'type'): mapType,
  ('type', 'beginBlock', 'var'): mapType,
  ('var', 'beginBlock', 'type'): mapType,
  ('var', 'beginBlock', 'var'): mapType,
  ('var', 'var'): typeDeclaration,
  ('type', 'var'): typeDeclaration,
  ('var', 'underline', 'var'): var,
  ('underline', 'var'): var,
  ('var', 'underline'): var,
  ('underline',): var,
  ('num', 'dot', 'num'): floatNumber,
  ('num', 'dot'): floatNumber,
  ('lparen', 'expr', 'rparen'): group,
  ('equal', 'equal'): operator,
  ('equal', 'operator'): operator,
  ('operator', 'equal'): operator,
  ('operator', 'operator'): operator,
  ('num',): expr,
  ('floatNumber',): expr,
  ('var',): expr,
  ('group',): expr,
  ('num', 'operator', 'num'): expr,
  ('num', 'operator', 'var'): expr,
  ('num', 'operator', 'expr'): expr,
  ('var', 'operator', 'num'): expr,
  ('var', 'operator', 'var'): expr,
  ('var', 'operator', 'expr'): expr,
  ('expr', 'operator', 'num'): expr,
  ('expr', 'operator', 'var'): expr,
  ('expr', 'operator', 'expr'): expr,
  ('operator', 'expr'): expr,
  ('expr', 'equal', 'expr'): assign,
  ('print', 'lparen', 'expr', 'rparen'): printFunc,
}