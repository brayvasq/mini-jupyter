
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVIDE EQUALS ID LPAREN MINUS NUMBER PLUS RPAREN SHOW TEXT TIMESquote : assignquote : exprassign : ID EQUALS exprexpr : expr PLUS termexpr : expr MINUS termexpr : expr DIVIDE termexpr : expr TIMES termexpr : termterm : NUMBERterm : SHOWterm : IDterm : TEXT'
    
_lr_action_items = {'ID':([0,9,10,11,12,13,],[4,15,15,15,15,15,]),'NUMBER':([0,9,10,11,12,13,],[6,6,6,6,6,6,]),'SHOW':([0,9,10,11,12,13,],[7,7,7,7,7,7,]),'TEXT':([0,9,10,11,12,13,],[8,8,8,8,8,8,]),'$end':([1,2,3,4,5,6,7,8,14,15,16,17,18,19,],[0,-1,-2,-11,-8,-9,-10,-12,-4,-11,-5,-6,-7,-3,]),'PLUS':([3,4,5,6,7,8,14,15,16,17,18,19,],[9,-11,-8,-9,-10,-12,-4,-11,-5,-6,-7,9,]),'MINUS':([3,4,5,6,7,8,14,15,16,17,18,19,],[10,-11,-8,-9,-10,-12,-4,-11,-5,-6,-7,10,]),'DIVIDE':([3,4,5,6,7,8,14,15,16,17,18,19,],[11,-11,-8,-9,-10,-12,-4,-11,-5,-6,-7,11,]),'TIMES':([3,4,5,6,7,8,14,15,16,17,18,19,],[12,-11,-8,-9,-10,-12,-4,-11,-5,-6,-7,12,]),'EQUALS':([4,],[13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'quote':([0,],[1,]),'assign':([0,],[2,]),'expr':([0,13,],[3,19,]),'term':([0,9,10,11,12,13,],[5,14,16,17,18,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> quote","S'",1,None,None,None),
  ('quote -> assign','quote',1,'p_quote_assign','parse.py',11),
  ('quote -> expr','quote',1,'p_quote_expr','parse.py',15),
  ('assign -> ID EQUALS expr','assign',3,'p_assign','parse.py',19),
  ('expr -> expr PLUS term','expr',3,'p_expr_sum','parse.py',24),
  ('expr -> expr MINUS term','expr',3,'p_expr_min','parse.py',31),
  ('expr -> expr DIVIDE term','expr',3,'p_expr_div','parse.py',38),
  ('expr -> expr TIMES term','expr',3,'p_expr_time','parse.py',45),
  ('expr -> term','expr',1,'p_expr_term','parse.py',52),
  ('term -> NUMBER','term',1,'p_term_num','parse.py',56),
  ('term -> SHOW','term',1,'p_command','parse.py',60),
  ('term -> ID','term',1,'p_term_id','parse.py',64),
  ('term -> TEXT','term',1,'p_term_text','parse.py',68),
]
