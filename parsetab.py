
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CIRCLE COMMA CONNECT DRAW EQUAL HEIGHT LPAREN NUMBER POINT RECTANGLE RPAREN SIZE SQUARE START TRIANGLE WEIGHT WORDS\n    draw : DRAW SQUARE\n        | DRAW SQUARE SIZE EQUAL NUMBER\n        | DRAW SQUARE START LPAREN NUMBER COMMA NUMBER RPAREN\n        | DRAW SQUARE START LPAREN NUMBER COMMA NUMBER RPAREN AND SIZE EQUAL NUMBER\n        | DRAW CIRCLE\n        | DRAW CIRCLE SIZE EQUAL NUMBER\n        | DRAW CIRCLE START LPAREN NUMBER COMMA NUMBER RPAREN\n        | DRAW CIRCLE START LPAREN NUMBER COMMA NUMBER RPAREN AND SIZE EQUAL NUMBER\n        | DRAW RECTANGLE\n        | DRAW RECTANGLE HEIGHT EQUAL NUMBER AND WEIGHT EQUAL NUMBER\n        | DRAW RECTANGLE START LPAREN NUMBER COMMA NUMBER RPAREN\n        | DRAW RECTANGLE START LPAREN NUMBER COMMA NUMBER RPAREN AND HEIGHT EQUAL NUMBER AND WEIGHT EQUAL NUMBER\n    \n    square : SQUARE\n    \n    circle : CIRCLE\n    '
    
_lr_action_items = {'DRAW':([0,],[2,]),'$end':([1,3,4,5,18,20,32,33,35,38,46,47,52,],[0,-1,-5,-9,-2,-6,-3,-7,-11,-10,-4,-8,-12,]),'SQUARE':([2,],[3,]),'CIRCLE':([2,],[4,]),'RECTANGLE':([2,],[5,]),'SIZE':([3,4,36,37,],[6,8,40,41,]),'START':([3,4,5,],[7,9,11,]),'HEIGHT':([5,39,],[10,42,]),'EQUAL':([6,8,10,30,40,41,42,50,],[12,14,16,34,43,44,45,51,]),'LPAREN':([7,9,11,],[13,15,17,]),'NUMBER':([12,13,14,15,16,17,24,25,27,34,43,44,45,51,],[18,19,20,21,22,23,28,29,31,38,46,47,48,52,]),'COMMA':([19,21,23,],[24,25,27,]),'AND':([22,32,33,35,48,],[26,36,37,39,49,]),'WEIGHT':([26,49,],[30,50,]),'RPAREN':([28,29,31,],[32,33,35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'draw':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> draw","S'",1,None,None,None),
  ('draw -> DRAW SQUARE','draw',2,'p_draw','A_sintatico.py',8),
  ('draw -> DRAW SQUARE SIZE EQUAL NUMBER','draw',5,'p_draw','A_sintatico.py',9),
  ('draw -> DRAW SQUARE START LPAREN NUMBER COMMA NUMBER RPAREN','draw',8,'p_draw','A_sintatico.py',10),
  ('draw -> DRAW SQUARE START LPAREN NUMBER COMMA NUMBER RPAREN AND SIZE EQUAL NUMBER','draw',12,'p_draw','A_sintatico.py',11),
  ('draw -> DRAW CIRCLE','draw',2,'p_draw','A_sintatico.py',12),
  ('draw -> DRAW CIRCLE SIZE EQUAL NUMBER','draw',5,'p_draw','A_sintatico.py',13),
  ('draw -> DRAW CIRCLE START LPAREN NUMBER COMMA NUMBER RPAREN','draw',8,'p_draw','A_sintatico.py',14),
  ('draw -> DRAW CIRCLE START LPAREN NUMBER COMMA NUMBER RPAREN AND SIZE EQUAL NUMBER','draw',12,'p_draw','A_sintatico.py',15),
  ('draw -> DRAW RECTANGLE','draw',2,'p_draw','A_sintatico.py',16),
  ('draw -> DRAW RECTANGLE HEIGHT EQUAL NUMBER AND WEIGHT EQUAL NUMBER','draw',9,'p_draw','A_sintatico.py',17),
  ('draw -> DRAW RECTANGLE START LPAREN NUMBER COMMA NUMBER RPAREN','draw',8,'p_draw','A_sintatico.py',18),
  ('draw -> DRAW RECTANGLE START LPAREN NUMBER COMMA NUMBER RPAREN AND HEIGHT EQUAL NUMBER AND WEIGHT EQUAL NUMBER','draw',16,'p_draw','A_sintatico.py',19),
  ('square -> SQUARE','square',1,'p_SQUARE','A_sintatico.py',29),
  ('circle -> CIRCLE','circle',1,'p_CIRCLE','A_sintatico.py',47),
]
