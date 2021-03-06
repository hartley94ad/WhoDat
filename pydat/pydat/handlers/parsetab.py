
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftANDORrightNOTleftCOLONAND COLON DATE FUZZY LPAREN NOT NULL OR QUOTED REGEX RPAREN WILDCARD WORDquery : LPAREN query RPARENquery : NOT queryquery : query query %prec ANDquery : query AND queryquery : query OR queryquery : specific\n             | daterange\n             | termqueryspecific : FUZZY WORD COLON WORDspecific : WORD COLON WORDspecific : FUZZY WORD COLON QUOTEDspecific : WORD COLON QUOTEDspecific : WORD COLON NULLspecific : WORD COLON WILDCARDspecific : WORD COLON REGEXdaterange : WORD COLON DATEdaterange : WORD COLON DATE COLON DATEtermquery : QUOTEDtermquery : WORD'
    
_lr_action_items = {'AND':([1,2,3,4,5,9,11,13,15,17,18,19,20,21,22,23,25,26,28,29,30,],[-19,-18,-7,-6,-8,14,14,-2,-3,-15,-10,-12,-14,-16,-13,-1,-4,-5,-9,-11,-17,]),'REGEX':([10,],[17,]),'NULL':([10,],[22,]),'WORD':([0,1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,],[1,-19,-18,-7,-6,-8,1,12,1,1,18,1,-2,1,-3,1,-15,-10,-12,-14,-16,-13,-1,28,-4,-5,-9,-11,-17,]),'WILDCARD':([10,],[20,]),'QUOTED':([0,1,2,3,4,5,6,8,9,10,11,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,],[2,-19,-18,-7,-6,-8,2,2,2,19,2,-2,2,-3,2,-15,-10,-12,-14,-16,-13,-1,29,-4,-5,-9,-11,-17,]),'DATE':([10,27,],[21,30,]),'COLON':([1,12,21,],[10,24,27,]),'LPAREN':([0,1,2,3,4,5,6,8,9,11,13,14,15,16,17,18,19,20,21,22,23,25,26,28,29,30,],[6,-19,-18,-7,-6,-8,6,6,6,6,-2,6,-3,6,-15,-10,-12,-14,-16,-13,-1,-4,-5,-9,-11,-17,]),'NOT':([0,1,2,3,4,5,6,8,9,11,13,14,15,16,17,18,19,20,21,22,23,25,26,28,29,30,],[8,-19,-18,-7,-6,-8,8,8,8,8,8,8,8,8,-15,-10,-12,-14,-16,-13,-1,8,8,-9,-11,-17,]),'FUZZY':([0,1,2,3,4,5,6,8,9,11,13,14,15,16,17,18,19,20,21,22,23,25,26,28,29,30,],[7,-19,-18,-7,-6,-8,7,7,7,7,-2,7,-3,7,-15,-10,-12,-14,-16,-13,-1,-4,-5,-9,-11,-17,]),'$end':([1,2,3,4,5,9,13,15,17,18,19,20,21,22,23,25,26,28,29,30,],[-19,-18,-7,-6,-8,0,-2,-3,-15,-10,-12,-14,-16,-13,-1,-4,-5,-9,-11,-17,]),'OR':([1,2,3,4,5,9,11,13,15,17,18,19,20,21,22,23,25,26,28,29,30,],[-19,-18,-7,-6,-8,16,16,-2,-3,-15,-10,-12,-14,-16,-13,-1,-4,-5,-9,-11,-17,]),'RPAREN':([1,2,3,4,5,11,13,15,17,18,19,20,21,22,23,25,26,28,29,30,],[-19,-18,-7,-6,-8,23,-2,-3,-15,-10,-12,-14,-16,-13,-1,-4,-5,-9,-11,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'specific':([0,6,8,9,11,13,14,15,16,25,26,],[4,4,4,4,4,4,4,4,4,4,4,]),'query':([0,6,8,9,11,13,14,15,16,25,26,],[9,11,13,15,15,15,25,15,26,15,15,]),'daterange':([0,6,8,9,11,13,14,15,16,25,26,],[3,3,3,3,3,3,3,3,3,3,3,]),'termquery':([0,6,8,9,11,13,14,15,16,25,26,],[5,5,5,5,5,5,5,5,5,5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> query","S'",1,None,None,None),
  ('query -> LPAREN query RPAREN','query',3,'p_query_group','advanced_es.py',296),
  ('query -> NOT query','query',2,'p_query_not','advanced_es.py',301),
  ('query -> query query','query',2,'p_query_query','advanced_es.py',324),
  ('query -> query AND query','query',3,'p_query_and_query','advanced_es.py',329),
  ('query -> query OR query','query',3,'p_query_or_query','advanced_es.py',334),
  ('query -> specific','query',1,'p_query_terminals','advanced_es.py',348),
  ('query -> daterange','query',1,'p_query_terminals','advanced_es.py',349),
  ('query -> termquery','query',1,'p_query_terminals','advanced_es.py',350),
  ('specific -> FUZZY WORD COLON WORD','specific',4,'p_specific_fuzzy_word','advanced_es.py',386),
  ('specific -> WORD COLON WORD','specific',3,'p_specific_word','advanced_es.py',403),
  ('specific -> FUZZY WORD COLON QUOTED','specific',4,'p_specific_fuzzy_quoted','advanced_es.py',415),
  ('specific -> WORD COLON QUOTED','specific',3,'p_specific_quoted','advanced_es.py',460),
  ('specific -> WORD COLON NULL','specific',3,'p_field_missing','advanced_es.py',519),
  ('specific -> WORD COLON WILDCARD','specific',3,'p_specific_wildcard','advanced_es.py',587),
  ('specific -> WORD COLON REGEX','specific',3,'p_specific_regex','advanced_es.py',596),
  ('daterange -> WORD COLON DATE','daterange',3,'p_daterange_single','advanced_es.py',621),
  ('daterange -> WORD COLON DATE COLON DATE','daterange',5,'p_daterange_range','advanced_es.py',634),
  ('termquery -> QUOTED','termquery',1,'p_termquery_quoted','advanced_es.py',650),
  ('termquery -> WORD','termquery',1,'p_termquery_word','advanced_es.py',703),
]
