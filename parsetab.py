
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOR_KWSHORT_CIRCUIT_OR_KWleftAND_KWSHORT_CIRCUIT_AND_KWleftEQleftLTGTLEGEleftPLUSMINUSleftMODleftTIMESDIVIDErightNOT_KWMINUS_MINUSPLUS_PLUSSHENASE INT FLOAT HARFE_SABET JAYEKHALI NOGHTE_VIRGUL COMMA COMMENT DOT PLUS MINUS TIMES DIVIDE MOD EQUALS PLUS_EQ MINUS_EQ TIMES_EQ DIVIDE_EQ COLON PLUS_PLUS MINUS_MINUS LT GT LE GE EQ OPEN_PAREN CLOSE_PAREN OPEN_BRACE CLOSE_BRACE OPEN_BRACKET CLOSE_BRACKET QUESTION_MARK PROGRAM_KW STRUCT_KW CONST_KW INT_KW FLOAT_KW BOOL_KW CHAR_KW IF_KW THEN_KW ELSE_KW SWITCH_KW END_KW CASE_KW DEFAULT_KW WHILE_KW RETURN_KW BREAK_KW OR_KW AND_KW SHORT_CIRCUIT_OR_KW SHORT_CIRCUIT_AND_KW NOT_KW TRUE_KW FALSE_KW MAIN barnameh : PROGRAM_KW SHENASE tarifha  tarifha : tarifha tarif  tarifha  :  tarif  tarif  : tarifeSakhtar  tarif : tarifeMoteghayyer  tarif : tarifeTabe  tarifeSakhtar : STRUCT_KW SHENASE OPEN_BRACE tarifhayeMahalli CLOSE_BRACE  tarifhayeMahalli : tarifhayeMahalli tarifMoteghayyereMahdud  tarifhayeMahalli : epsilon  tarifMoteghayyereMahdud : jenseMahdud tarifhayeMoteghayyerha NOGHTE_VIRGUL  jenseMahdud : CONST_KW jens  jenseMahdud : jens  jens : INT_KW  jens : FLOAT_KW  jens : BOOL_KW  jens : CHAR_KW  tarifeMoteghayyer : jens tarifhayeMoteghayyerha NOGHTE_VIRGUL  tarifhayeMoteghayyerha : tarifeMeghdareAvvalie  tarifhayeMoteghayyerha : tarifhayeMoteghayyerha COMMA tarifeMeghdareAvvalie  tarifeMeghdareAvvalie : tarifeShenaseyeMoteghayyer  tarifeMeghdareAvvalie : tarifeShenaseyeMoteghayyer EQUALS ebarateSade  tarifeShenaseyeMoteghayyer : SHENASE  tarifeShenaseyeMoteghayyer : SHENASE OPEN_BRACKET INT CLOSE_BRACKET  tarifeShenaseyeMoteghayyer : SHENASE OPEN_BRACKET FLOAT CLOSE_BRACKET  tarifeTabe : jens SHENASE   OPEN_PAREN  vorudi   CLOSE_PAREN  jomle  tarifeTabe : SHENASE   OPEN_PAREN  vorudi   CLOSE_PAREN  jomle  vorudi : vorudiha  vorudi : epsilon  vorudiha : vorudiha NOGHTE_VIRGUL jensVorudiha  vorudiha : jensVorudiha  jensVorudiha : jens shenaseyeVorudiha  shenaseyeVorudiha : shenaseyeVorudiha COMMA shenaseyeVorudi  shenaseyeVorudiha : shenaseyeVorudi  shenaseyeVorudi : SHENASE  shenaseyeVorudi : SHENASE OPEN_BRACKET CLOSE_BRACKET  jomle : jomleyeMorakkab  jomle : jomleyeEbarat  jomle : jomleyeEntekhab  jomle : jomleyeTekrar  jomle : jomleyeBazgasht  jomle : jomleyeShekast  jomleyeMorakkab : OPEN_BRACE tarifhayeMahalli jomleha CLOSE_BRACE  jomleha : jomleha jomle  jomleha : epsilon  jomleyeEbarat : ebarat NOGHTE_VIRGUL  jomleyeEbarat : NOGHTE_VIRGUL  jomleyeEntekhab : IF_KW ebarateSade THEN_KW jomle  jomleyeEntekhab : IF_KW ebarateSade THEN_KW jomle ELSE_KW jomle  jomleyeEntekhab : SWITCH_KW OPEN_PAREN  ebarateSade CLOSE_PAREN  onsoreHalat onsorePishfarz END_KW  onsoreHalat : CASE_KW INT COLON jomle NOGHTE_VIRGUL  onsoreHalat : CASE_KW FLOAT COLON jomle NOGHTE_VIRGUL  onsoreHalat : onsoreHalat CASE_KW INT COLON jomle NOGHTE_VIRGUL  onsoreHalat : onsoreHalat CASE_KW FLOAT COLON jomle NOGHTE_VIRGUL  onsorePishfarz : DEFAULT_KW COLON jomle NOGHTE_VIRGUL  onsorePishfarz :  epsilon  jomleyeTekrar : WHILE_KW OPEN_PAREN  ebarateSade   CLOSE_PAREN  jomle    jomleyeBazgasht :  RETURN_KW  NOGHTE_VIRGUL  jomleyeBazgasht : RETURN_KW ebarat NOGHTE_VIRGUL  jomleyeShekast : BREAK_KW NOGHTE_VIRGUL  ebarat : taghirpazir EQUALS ebarat  ebarat : taghirpazir PLUS_EQ ebarat  ebarat : taghirpazir MINUS_EQ ebarat  ebarat : taghirpazir TIMES_EQ ebarat  ebarat : taghirpazir DIVIDE_EQ ebarat  ebarat : taghirpazir PLUS_PLUS ebarat : taghirpazir MINUS_MINUS  ebarat : ebarateSade  ebarateSade : ebarateSade OR_KW ebarateSade  ebarateSade : ebarateSade AND_KW ebarateSade  ebarateSade : ebarateSade SHORT_CIRCUIT_OR_KW ebarateSade  ebarateSade : ebarateSade SHORT_CIRCUIT_AND_KW ebarateSade  ebarateSade : NOT_KW ebarateSade  ebarateSade : ebarateRabetei  ebarateRabetei : ebarateRiaziManteghi  ebarateRabetei : ebarateRiaziManteghi amalgareRabetei ebarateRiaziManteghi  amalgareRabetei : LT   amalgareRabetei : GT   amalgareRabetei : GE  amalgareRabetei : LE  amalgareRabetei : EQ  ebarateRiaziManteghi : ebarateYegani ebarateRiaziManteghi : ebarateRiaziManteghi amalgareRiazi ebarateRiaziManteghi  amalgareRiazi : PLUS  amalgareRiazi : MINUS  amalgareRiazi : TIMES  amalgareRiazi : DIVIDE  amalgareRiazi : MOD  ebarateYegani : amalgareYegani ebarateYegani  ebarateYegani : amel  amalgareYegani : MINUS  amalgareYegani : TIMES  amalgareYegani : QUESTION_MARK  amel : taghirpazir  amel :  taghirnapazir  taghirpazir : SHENASE  taghirpazir : taghirpazir OPEN_BRACKET ebarat CLOSE_BRACKET taghirpazir : taghirpazir DOT SHENASE  taghirnapazir : OPEN_PAREN ebarat CLOSE_PAREN  taghirnapazir : sedaZadan taghirnapazir : meghdareSabet  sedaZadan : SHENASE OPEN_PAREN bordareVorudi CLOSE_PAREN  bordareVorudi : bordareVorudiha  bordareVorudi : epsilon  bordareVorudiha : bordareVorudiha COMMA ebarat bordareVorudiha : ebarat  meghdareSabet : INT  meghdareSabet :  FLOAT  meghdareSabet :  HARFE_SABET  meghdareSabet : TRUE_KW  meghdareSabet : FALSE_KW  epsilon : '
    
_lr_action_items = {'WHILE_KW':([61,65,67,94,103,106,107,108,109,112,114,115,145,146,147,149,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[-9,101,101,-8,-36,-41,-37,-39,-40,-38,-111,-46,-57,-45,-59,-111,-10,-58,101,101,-44,101,-47,-42,-43,-56,101,-48,101,101,101,-49,101,101,]),'THEN_KW':([37,39,41,42,43,45,46,47,49,50,51,54,55,57,70,86,118,126,127,132,133,134,135,136,148,155,157,],[-81,-89,-73,-99,-106,-110,-107,-109,-94,-100,-74,-108,-95,-93,-88,-72,-98,-75,-82,-70,-68,-71,-69,-97,162,-101,-96,]),'$end':([2,7,8,10,12,13,20,26,98,103,106,107,108,109,110,112,115,117,145,146,147,161,168,169,171,181,187,],[0,-3,-5,-1,-6,-4,-2,-17,-7,-36,-41,-37,-39,-40,-26,-38,-46,-25,-57,-45,-59,-58,-47,-42,-56,-48,-49,]),'SWITCH_KW':([61,65,67,94,103,106,107,108,109,112,114,115,145,146,147,149,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[-9,102,102,-8,-36,-41,-37,-39,-40,-38,-111,-46,-57,-45,-59,-111,-10,-58,102,102,-44,102,-47,-42,-43,-56,102,-48,102,102,102,-49,102,102,]),'MINUS':([25,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,61,65,67,70,72,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,91,93,94,103,104,106,107,108,109,112,113,114,115,118,119,120,122,123,124,126,127,136,142,143,145,146,147,149,155,156,157,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[38,-81,-90,-89,-91,-99,-106,38,-110,-107,-109,38,-94,-100,77,-92,38,-108,-95,-93,-9,38,38,-88,-93,38,38,-77,-84,-78,-76,-79,-86,-83,-85,-80,-87,38,38,38,38,38,38,-8,-36,38,-41,-37,-39,-40,-38,38,-111,-46,-98,38,38,38,38,38,77,77,-97,38,38,-57,-45,-59,-111,-101,38,-96,-10,-58,38,38,-44,38,-47,-42,-43,-56,38,-48,38,38,38,-49,38,38,]),'SHORT_CIRCUIT_OR_KW':([37,39,41,42,43,45,46,47,49,50,51,54,55,56,57,70,72,73,86,118,126,127,132,133,134,135,136,148,155,157,159,160,],[-81,-89,-73,-99,-106,-110,-107,-109,-94,-100,-74,-108,-95,88,-93,-88,-93,88,-72,-98,-75,-82,-70,-68,-71,-69,-97,88,-101,-96,88,88,]),'PROGRAM_KW':([0,],[1,]),'PLUS_EQ':([55,72,136,157,],[-95,119,-97,-96,]),'ELSE_KW':([103,106,107,108,109,112,115,145,146,147,161,168,169,171,181,187,],[-36,-41,-37,-39,-40,-38,-46,-57,-45,-59,-58,174,-42,-56,-48,-49,]),'GT':([37,39,42,43,45,46,47,49,50,51,54,55,57,70,72,118,127,136,155,157,],[-81,-89,-99,-106,-110,-107,-109,-94,-100,76,-108,-95,-93,-88,-93,-98,-82,-97,-101,-96,]),'CLOSE_BRACE':([28,60,61,94,103,106,107,108,109,112,114,115,145,146,147,149,158,161,163,164,168,169,170,171,181,187,],[-111,98,-9,-8,-36,-41,-37,-39,-40,-38,-111,-46,-57,-45,-59,-111,-10,-58,169,-44,-47,-42,-43,-56,-48,-49,]),'MOD':([37,39,42,43,45,46,47,49,50,51,54,55,57,70,72,118,126,127,136,155,157,],[-81,-89,-99,-106,-110,-107,-109,-94,-100,85,-108,-95,-93,-88,-93,-98,85,85,-97,-101,-96,]),'RETURN_KW':([61,65,67,94,103,106,107,108,109,112,114,115,145,146,147,149,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[-9,104,104,-8,-36,-41,-37,-39,-40,-38,-111,-46,-57,-45,-59,-111,-10,-58,104,104,-44,104,-47,-42,-43,-56,104,-48,104,104,104,-49,104,104,]),'CONST_KW':([28,60,61,94,114,149,158,],[-111,97,-9,-8,-111,97,-10,]),'FALSE_KW':([25,38,40,44,48,52,53,61,65,67,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,91,93,94,103,104,106,107,108,109,112,113,114,115,119,120,122,123,124,142,143,145,146,147,149,156,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[45,-90,-91,45,45,-92,45,-9,45,45,45,45,-77,-84,-78,-76,-79,-86,-83,-85,-80,-87,45,45,45,45,45,45,-8,-36,45,-41,-37,-39,-40,-38,45,-111,-46,45,45,45,45,45,45,45,-57,-45,-59,-111,45,-10,-58,45,45,-44,45,-47,-42,-43,-56,45,-48,45,45,45,-49,45,45,]),'OPEN_BRACKET':([16,55,57,58,62,72,136,157,],[24,-95,93,24,99,93,-97,-96,]),'MINUS_EQ':([55,72,136,157,],[-95,120,-97,-96,]),'LT':([37,39,42,43,45,46,47,49,50,51,54,55,57,70,72,118,127,136,155,157,],[-81,-89,-99,-106,-110,-107,-109,-94,-100,79,-108,-95,-93,-88,-93,-98,-82,-97,-101,-96,]),'DIVIDE_EQ':([55,72,136,157,],[-95,122,-97,-96,]),'HARFE_SABET':([25,38,40,44,48,52,53,61,65,67,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,91,93,94,103,104,106,107,108,109,112,113,114,115,119,120,122,123,124,142,143,145,146,147,149,156,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[54,-90,-91,54,54,-92,54,-9,54,54,54,54,-77,-84,-78,-76,-79,-86,-83,-85,-80,-87,54,54,54,54,54,54,-8,-36,54,-41,-37,-39,-40,-38,54,-111,-46,54,54,54,54,54,54,54,-57,-45,-59,-111,54,-10,-58,54,54,-44,54,-47,-42,-43,-56,54,-48,54,54,54,-49,54,54,]),'INT_KW':([3,7,8,10,12,13,20,22,23,26,28,60,61,66,94,97,98,103,106,107,108,109,110,112,114,115,117,145,146,147,149,158,161,168,169,171,181,187,],[14,-3,-5,14,-6,-4,-2,14,14,-17,-111,14,-9,14,-8,14,-7,-36,-41,-37,-39,-40,-26,-38,-111,-46,-25,-57,-45,-59,14,-10,-58,-47,-42,-56,-48,-49,]),'PLUS':([37,39,42,43,45,46,47,49,50,51,54,55,57,70,72,118,126,127,136,155,157,],[-81,-89,-99,-106,-110,-107,-109,-94,-100,82,-108,-95,-93,-88,-93,-98,82,82,-97,-101,-96,]),'SHORT_CIRCUIT_AND_KW':([37,39,41,42,43,45,46,47,49,50,51,54,55,56,57,70,72,73,86,118,126,127,132,133,134,135,136,148,155,157,159,160,],[-81,-89,-73,-99,-106,-110,-107,-109,-94,-100,-74,-108,-95,90,-93,-88,-93,90,-72,-98,-75,-82,90,90,-71,-69,-97,90,-101,-96,90,90,]),'OR_KW':([37,39,41,42,43,45,46,47,49,50,51,54,55,56,57,70,72,73,86,118,126,127,132,133,134,135,136,148,155,157,159,160,],[-81,-89,-73,-99,-106,-110,-107,-109,-94,-100,-74,-108,-95,89,-93,-88,-93,89,-72,-98,-75,-82,-70,-68,-71,-69,-97,89,-101,-96,89,89,]),'CLOSE_BRACKET':([35,36,37,39,41,42,43,45,46,47,49,50,51,54,55,57,70,72,73,86,99,118,121,125,126,127,132,133,134,135,136,137,150,151,152,153,154,155,157,],[68,69,-81,-89,-73,-99,-106,-110,-107,-109,-94,-100,-74,-108,-95,-93,-88,-93,-67,-72,140,-98,-65,-66,-75,-82,-70,-68,-71,-69,-97,157,-61,-62,-64,-63,-60,-101,-96,]),'SHENASE':([1,3,4,5,6,7,8,9,10,11,12,13,14,20,25,26,27,31,38,40,44,48,52,53,61,65,67,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,98,100,103,104,106,107,108,109,110,112,113,114,115,117,119,120,122,123,124,139,142,143,145,146,147,149,156,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[3,15,-16,-15,16,-3,-5,-14,15,21,-6,-4,-13,-2,55,-17,58,62,-90,-91,55,55,-92,55,-9,55,55,55,55,-77,-84,-78,-76,-79,-86,-83,-85,-80,-87,55,55,55,55,55,136,55,-8,-12,58,-7,62,-36,55,-41,-37,-39,-40,-26,-38,55,-111,-46,-25,55,55,55,55,55,-11,55,55,-57,-45,-59,-111,55,-10,-58,55,55,-44,55,-47,-42,-43,-56,55,-48,55,55,55,-49,55,55,]),'AND_KW':([37,39,41,42,43,45,46,47,49,50,51,54,55,56,57,70,72,73,86,118,126,127,132,133,134,135,136,148,155,157,159,160,],[-81,-89,-73,-99,-106,-110,-107,-109,-94,-100,-74,-108,-95,91,-93,-88,-93,91,-72,-98,-75,-82,91,91,-71,-69,-97,91,-101,-96,91,91,]),'END_KW':([173,177,180,193,194,197,198,199,],[-111,-55,187,-51,-50,-54,-53,-52,]),'DOT':([55,57,72,136,157,],[-95,92,92,-97,-96,]),'CHAR_KW':([3,7,8,10,12,13,20,22,23,26,28,60,61,66,94,97,98,103,106,107,108,109,110,112,114,115,117,145,146,147,149,158,161,168,169,171,181,187,],[4,-3,-5,4,-6,-4,-2,4,4,-17,-111,4,-9,4,-8,4,-7,-36,-41,-37,-39,-40,-26,-38,-111,-46,-25,-57,-45,-59,4,-10,-58,-47,-42,-56,-48,-49,]),'BOOL_KW':([3,7,8,10,12,13,20,22,23,26,28,60,61,66,94,97,98,103,106,107,108,109,110,112,114,115,117,145,146,147,149,158,161,168,169,171,181,187,],[5,-3,-5,5,-6,-4,-2,5,5,-17,-111,5,-9,5,-8,5,-7,-36,-41,-37,-39,-40,-26,-38,-111,-46,-25,-57,-45,-59,5,-10,-58,-47,-42,-56,-48,-49,]),'OPEN_PAREN':([15,16,25,38,40,44,48,52,53,55,61,65,67,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,91,93,94,101,102,103,104,106,107,108,109,112,113,114,115,119,120,122,123,124,142,143,145,146,147,149,156,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[22,23,48,-90,-91,48,48,-92,48,87,-9,48,48,48,48,-77,-84,-78,-76,-79,-86,-83,-85,-80,-87,48,48,48,48,48,48,-8,142,143,-36,48,-41,-37,-39,-40,-38,48,-111,-46,48,48,48,48,48,48,48,-57,-45,-59,-111,48,-10,-58,48,48,-44,48,-47,-42,-43,-56,48,-48,48,48,48,-49,48,48,]),'COMMA':([16,17,18,19,37,39,41,42,43,45,46,47,49,50,51,54,55,56,57,58,59,62,63,64,68,69,70,72,73,86,118,121,125,126,127,129,131,132,133,134,135,136,138,140,141,150,151,152,153,154,155,157,165,],[-22,-20,-18,27,-81,-89,-73,-99,-106,-110,-107,-109,-94,-100,-74,-108,-95,-21,-93,-22,-19,-34,-33,100,-23,-24,-88,-93,-67,-72,-98,-65,-66,-75,-82,-105,156,-70,-68,-71,-69,-97,27,-35,-32,-61,-62,-64,-63,-60,-101,-96,-104,]),'FLOAT_KW':([3,7,8,10,12,13,20,22,23,26,28,60,61,66,94,97,98,103,106,107,108,109,110,112,114,115,117,145,146,147,149,158,161,168,169,171,181,187,],[9,-3,-5,9,-6,-4,-2,9,9,-17,-111,9,-9,9,-8,9,-7,-36,-41,-37,-39,-40,-26,-38,-111,-46,-25,-57,-45,-59,9,-10,-58,-47,-42,-56,-48,-49,]),'TIMES':([25,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,61,65,67,70,72,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,91,93,94,103,104,106,107,108,109,112,113,114,115,118,119,120,122,123,124,126,127,136,142,143,145,146,147,149,155,156,157,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[40,-81,-90,-89,-91,-99,-106,40,-110,-107,-109,40,-94,-100,83,-92,40,-108,-95,-93,-9,40,40,-88,-93,40,40,-77,-84,-78,-76,-79,-86,-83,-85,-80,-87,40,40,40,40,40,40,-8,-36,40,-41,-37,-39,-40,-38,40,-111,-46,-98,40,40,40,40,40,83,83,-97,40,40,-57,-45,-59,-111,-101,40,-96,-10,-58,40,40,-44,40,-47,-42,-43,-56,40,-48,40,40,40,-49,40,40,]),'INT':([24,25,38,40,44,48,52,53,61,65,67,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,91,93,94,103,104,106,107,108,109,112,113,114,115,119,120,122,123,124,142,143,145,146,147,149,156,158,161,162,163,164,166,168,169,170,171,172,174,178,181,182,183,186,187,190,191,],[35,43,-90,-91,43,43,-92,43,-9,43,43,43,43,-77,-84,-78,-76,-79,-86,-83,-85,-80,-87,43,43,43,43,43,43,-8,-36,43,-41,-37,-39,-40,-38,43,-111,-46,43,43,43,43,43,43,43,-57,-45,-59,-111,43,-10,-58,43,43,-44,43,-47,-42,-43,-56,176,43,185,-48,43,43,43,-49,43,43,]),'PLUS_PLUS':([55,72,136,157,],[-95,121,-97,-96,]),'LE':([37,39,42,43,45,46,47,49,50,51,54,55,57,70,72,118,127,136,155,157,],[-81,-89,-99,-106,-110,-107,-109,-94,-100,80,-108,-95,-93,-88,-93,-98,-82,-97,-101,-96,]),'TIMES_EQ':([55,72,136,157,],[-95,123,-97,-96,]),'DIVIDE':([37,39,42,43,45,46,47,49,50,51,54,55,57,70,72,118,126,127,136,155,157,],[-81,-89,-99,-106,-110,-107,-109,-94,-100,81,-108,-95,-93,-88,-93,-98,81,81,-97,-101,-96,]),'FLOAT':([24,25,38,40,44,48,52,53,61,65,67,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,91,93,94,103,104,106,107,108,109,112,113,114,115,119,120,122,123,124,142,143,145,146,147,149,156,158,161,162,163,164,166,168,169,170,171,172,174,178,181,182,183,186,187,190,191,],[36,46,-90,-91,46,46,-92,46,-9,46,46,46,46,-77,-84,-78,-76,-79,-86,-83,-85,-80,-87,46,46,46,46,46,46,-8,-36,46,-41,-37,-39,-40,-38,46,-111,-46,46,46,46,46,46,46,46,-57,-45,-59,-111,46,-10,-58,46,46,-44,46,-47,-42,-43,-56,175,46,184,-48,46,46,46,-49,46,46,]),'CASE_KW':([167,173,193,194,198,199,],[172,178,-51,-50,-53,-52,]),'MINUS_MINUS':([55,72,136,157,],[-95,125,-97,-96,]),'EQ':([37,39,42,43,45,46,47,49,50,51,54,55,57,70,72,118,127,136,155,157,],[-81,-89,-99,-106,-110,-107,-109,-94,-100,84,-108,-95,-93,-88,-93,-98,-82,-97,-101,-96,]),'STRUCT_KW':([3,7,8,10,12,13,20,26,98,103,106,107,108,109,110,112,115,117,145,146,147,161,168,169,171,181,187,],[11,-3,-5,11,-6,-4,-2,-17,-7,-36,-41,-37,-39,-40,-26,-38,-46,-25,-57,-45,-59,-58,-47,-42,-56,-48,-49,]),'TRUE_KW':([25,38,40,44,48,52,53,61,65,67,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,91,93,94,103,104,106,107,108,109,112,113,114,115,119,120,122,123,124,142,143,145,146,147,149,156,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[47,-90,-91,47,47,-92,47,-9,47,47,47,47,-77,-84,-78,-76,-79,-86,-83,-85,-80,-87,47,47,47,47,47,47,-8,-36,47,-41,-37,-39,-40,-38,47,-111,-46,47,47,47,47,47,47,47,-57,-45,-59,-111,47,-10,-58,47,47,-44,47,-47,-42,-43,-56,47,-48,47,47,47,-49,47,47,]),'EQUALS':([16,17,55,58,68,69,72,136,157,],[-22,25,-95,-22,-23,-24,124,-97,-96,]),'BREAK_KW':([61,65,67,94,103,106,107,108,109,112,114,115,145,146,147,149,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[-9,111,111,-8,-36,-41,-37,-39,-40,-38,-111,-46,-57,-45,-59,-111,-10,-58,111,111,-44,111,-47,-42,-43,-56,111,-48,111,111,111,-49,111,111,]),'GE':([37,39,42,43,45,46,47,49,50,51,54,55,57,70,72,118,127,136,155,157,],[-81,-89,-99,-106,-110,-107,-109,-94,-100,78,-108,-95,-93,-88,-93,-98,-82,-97,-101,-96,]),'QUESTION_MARK':([25,38,40,44,48,52,53,61,65,67,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,91,93,94,103,104,106,107,108,109,112,113,114,115,119,120,122,123,124,142,143,145,146,147,149,156,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[52,-90,-91,52,52,-92,52,-9,52,52,52,52,-77,-84,-78,-76,-79,-86,-83,-85,-80,-87,52,52,52,52,52,52,-8,-36,52,-41,-37,-39,-40,-38,52,-111,-46,52,52,52,52,52,52,52,-57,-45,-59,-111,52,-10,-58,52,52,-44,52,-47,-42,-43,-56,52,-48,52,52,52,-49,52,52,]),'NOT_KW':([25,48,53,61,65,67,87,88,89,90,91,93,94,103,104,106,107,108,109,112,113,114,115,119,120,122,123,124,142,143,145,146,147,149,156,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[53,53,53,-9,53,53,53,53,53,53,53,53,-8,-36,53,-41,-37,-39,-40,-38,53,-111,-46,53,53,53,53,53,53,53,-57,-45,-59,-111,53,-10,-58,53,53,-44,53,-47,-42,-43,-56,53,-48,53,53,53,-49,53,53,]),'IF_KW':([61,65,67,94,103,106,107,108,109,112,114,115,145,146,147,149,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[-9,113,113,-8,-36,-41,-37,-39,-40,-38,-111,-46,-57,-45,-59,-111,-10,-58,113,113,-44,113,-47,-42,-43,-56,113,-48,113,113,113,-49,113,113,]),'DEFAULT_KW':([173,193,194,198,199,],[179,-51,-50,-53,-52,]),'CLOSE_PAREN':([22,23,29,30,32,33,34,37,39,41,42,43,45,46,47,49,50,51,54,55,57,62,63,64,70,71,72,73,86,87,116,118,121,125,126,127,128,129,130,131,132,133,134,135,136,140,141,150,151,152,153,154,155,157,159,160,165,],[-111,-111,-30,-28,65,-27,67,-81,-89,-73,-99,-106,-110,-107,-109,-94,-100,-74,-108,-95,-93,-34,-33,-31,-88,118,-93,-67,-72,-111,-29,-98,-65,-66,-75,-82,-103,-105,155,-102,-70,-68,-71,-69,-97,-35,-32,-61,-62,-64,-63,-60,-101,-96,166,167,-104,]),'OPEN_BRACE':([21,61,65,67,94,103,106,107,108,109,112,114,115,145,146,147,149,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,190,191,],[28,-9,114,114,-8,-36,-41,-37,-39,-40,-38,-111,-46,-57,-45,-59,-111,-10,-58,114,114,-44,114,-47,-42,-43,-56,114,-48,114,114,114,-49,114,114,]),'COLON':([175,176,179,184,185,],[182,183,186,190,191,]),'NOGHTE_VIRGUL':([16,17,18,19,29,33,37,39,41,42,43,45,46,47,49,50,51,54,55,56,57,58,59,61,62,63,64,65,67,68,69,70,72,73,86,94,103,104,105,106,107,108,109,111,112,114,115,116,118,121,125,126,127,132,133,134,135,136,138,140,141,144,145,146,147,149,150,151,152,153,154,155,157,158,161,162,163,164,166,168,169,170,171,174,181,182,183,186,187,188,189,190,191,192,195,196,],[-22,-20,-18,26,-30,66,-81,-89,-73,-99,-106,-110,-107,-109,-94,-100,-74,-108,-95,-21,-93,-22,-19,-9,-34,-33,-31,115,115,-23,-24,-88,-93,-67,-72,-8,-36,145,146,-41,-37,-39,-40,147,-38,-111,-46,-29,-98,-65,-66,-75,-82,-70,-68,-71,-69,-97,158,-35,-32,161,-57,-45,-59,-111,-61,-62,-64,-63,-60,-101,-96,-10,-58,115,115,-44,115,-47,-42,-43,-56,115,-48,115,115,115,-49,193,194,115,115,197,198,199,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ebarateYegani':([25,44,48,53,65,67,74,75,87,88,89,90,91,93,104,113,119,120,122,123,124,142,143,156,162,163,166,174,182,183,186,190,191,],[37,70,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'tarifeTabe':([3,10,],[12,12,]),'amel':([25,44,48,53,65,67,74,75,87,88,89,90,91,93,104,113,119,120,122,123,124,142,143,156,162,163,166,174,182,183,186,190,191,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'tarifeMoteghayyer':([3,10,],[8,8,]),'amalgareYegani':([25,44,48,53,65,67,74,75,87,88,89,90,91,93,104,113,119,120,122,123,124,142,143,156,162,163,166,174,182,183,186,190,191,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'jomleyeMorakkab':([65,67,162,163,166,174,182,183,186,190,191,],[103,103,103,103,103,103,103,103,103,103,103,]),'tarifeMeghdareAvvalie':([6,27,96,],[18,59,18,]),'onsorePishfarz':([173,],[180,]),'meghdareSabet':([25,44,48,53,65,67,74,75,87,88,89,90,91,93,104,113,119,120,122,123,124,142,143,156,162,163,166,174,182,183,186,190,191,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'tarifMoteghayyereMahdud':([60,149,],[94,94,]),'ebarat':([48,65,67,87,93,104,119,120,122,123,124,156,162,163,166,174,182,183,186,190,191,],[71,105,105,129,137,144,150,151,152,153,154,165,105,105,105,105,105,105,105,105,105,]),'bordareVorudi':([87,],[130,]),'vorudiha':([22,23,],[33,33,]),'jomleha':([149,],[163,]),'tarif':([3,10,],[7,20,]),'jomleyeEbarat':([65,67,162,163,166,174,182,183,186,190,191,],[107,107,107,107,107,107,107,107,107,107,107,]),'tarifeShenaseyeMoteghayyer':([6,27,96,],[17,17,17,]),'jomleyeTekrar':([65,67,162,163,166,174,182,183,186,190,191,],[108,108,108,108,108,108,108,108,108,108,108,]),'ebarateRiaziManteghi':([25,48,53,65,67,74,75,87,88,89,90,91,93,104,113,119,120,122,123,124,142,143,156,162,163,166,174,182,183,186,190,191,],[51,51,51,51,51,126,127,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'jomle':([65,67,162,163,166,174,182,183,186,190,191,],[110,117,168,170,171,181,188,189,192,195,196,]),'epsilon':([22,23,28,87,114,149,173,],[30,30,61,128,61,164,177,]),'jensVorudiha':([22,23,66,],[29,29,116,]),'ebarateRabetei':([25,48,53,65,67,87,88,89,90,91,93,104,113,119,120,122,123,124,142,143,156,162,163,166,174,182,183,186,190,191,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'shenaseyeVorudi':([31,100,],[63,141,]),'jens':([3,10,22,23,60,66,97,149,],[6,6,31,31,95,31,139,95,]),'amalgareRiazi':([51,126,127,],[75,75,75,]),'jenseMahdud':([60,149,],[96,96,]),'jomleyeBazgasht':([65,67,162,163,166,174,182,183,186,190,191,],[109,109,109,109,109,109,109,109,109,109,109,]),'amalgareRabetei':([51,],[74,]),'sedaZadan':([25,44,48,53,65,67,74,75,87,88,89,90,91,93,104,113,119,120,122,123,124,142,143,156,162,163,166,174,182,183,186,190,191,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'tarifha':([3,],[10,]),'onsoreHalat':([167,],[173,]),'tarifhayeMoteghayyerha':([6,96,],[19,138,]),'tarifhayeMahalli':([28,114,],[60,149,]),'taghirnapazir':([25,44,48,53,65,67,74,75,87,88,89,90,91,93,104,113,119,120,122,123,124,142,143,156,162,163,166,174,182,183,186,190,191,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'jomleyeShekast':([65,67,162,163,166,174,182,183,186,190,191,],[106,106,106,106,106,106,106,106,106,106,106,]),'jomleyeEntekhab':([65,67,162,163,166,174,182,183,186,190,191,],[112,112,112,112,112,112,112,112,112,112,112,]),'shenaseyeVorudiha':([31,],[64,]),'tarifeSakhtar':([3,10,],[13,13,]),'bordareVorudiha':([87,],[131,]),'vorudi':([22,23,],[32,34,]),'barnameh':([0,],[2,]),'taghirpazir':([25,44,48,53,65,67,74,75,87,88,89,90,91,93,104,113,119,120,122,123,124,142,143,156,162,163,166,174,182,183,186,190,191,],[57,57,72,57,72,72,57,57,72,57,57,57,57,72,72,57,72,72,72,72,72,57,57,72,72,72,72,72,72,72,72,72,72,]),'ebarateSade':([25,48,53,65,67,87,88,89,90,91,93,104,113,119,120,122,123,124,142,143,156,162,163,166,174,182,183,186,190,191,],[56,73,86,73,73,73,132,133,134,135,73,73,148,73,73,73,73,73,159,160,73,73,73,73,73,73,73,73,73,73,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> barnameh","S'",1,None,None,None),
  ('barnameh -> PROGRAM_KW SHENASE tarifha','barnameh',3,'p_barnameh','yacc.py',17),
  ('tarifha -> tarifha tarif','tarifha',2,'p_tarifha_1','yacc.py',22),
  ('tarifha -> tarif','tarifha',1,'p_tarifha_2','yacc.py',27),
  ('tarif -> tarifeSakhtar','tarif',1,'p_tarif_1','yacc.py',33),
  ('tarif -> tarifeMoteghayyer','tarif',1,'p_tarif_2','yacc.py',38),
  ('tarif -> tarifeTabe','tarif',1,'p_tarif_3','yacc.py',43),
  ('tarifeSakhtar -> STRUCT_KW SHENASE OPEN_BRACE tarifhayeMahalli CLOSE_BRACE','tarifeSakhtar',5,'p_tarifeSakhtar','yacc.py',48),
  ('tarifhayeMahalli -> tarifhayeMahalli tarifMoteghayyereMahdud','tarifhayeMahalli',2,'p_tarifhayeMahalli_1','yacc.py',53),
  ('tarifhayeMahalli -> epsilon','tarifhayeMahalli',1,'p_tarifhayeMahalli_2','yacc.py',58),
  ('tarifMoteghayyereMahdud -> jenseMahdud tarifhayeMoteghayyerha NOGHTE_VIRGUL','tarifMoteghayyereMahdud',3,'p_tarifMoteghayyereMahdud','yacc.py',63),
  ('jenseMahdud -> CONST_KW jens','jenseMahdud',2,'p_jenseMahdud_1','yacc.py',68),
  ('jenseMahdud -> jens','jenseMahdud',1,'p_jenseMahdud_2','yacc.py',73),
  ('jens -> INT_KW','jens',1,'p_jens_1','yacc.py',78),
  ('jens -> FLOAT_KW','jens',1,'p_jens_2','yacc.py',83),
  ('jens -> BOOL_KW','jens',1,'p_jens_3','yacc.py',88),
  ('jens -> CHAR_KW','jens',1,'p_jens_4','yacc.py',93),
  ('tarifeMoteghayyer -> jens tarifhayeMoteghayyerha NOGHTE_VIRGUL','tarifeMoteghayyer',3,'p_tarifeMoteghayyer','yacc.py',98),
  ('tarifhayeMoteghayyerha -> tarifeMeghdareAvvalie','tarifhayeMoteghayyerha',1,'p_tarifhayeMoteghayyerha_1','yacc.py',103),
  ('tarifhayeMoteghayyerha -> tarifhayeMoteghayyerha COMMA tarifeMeghdareAvvalie','tarifhayeMoteghayyerha',3,'p_tarifhayeMoteghayyerha_2','yacc.py',108),
  ('tarifeMeghdareAvvalie -> tarifeShenaseyeMoteghayyer','tarifeMeghdareAvvalie',1,'p_tarifeMeghdareAvvalie_1','yacc.py',113),
  ('tarifeMeghdareAvvalie -> tarifeShenaseyeMoteghayyer EQUALS ebarateSade','tarifeMeghdareAvvalie',3,'p_tarifeMeghdareAvvalie_2','yacc.py',118),
  ('tarifeShenaseyeMoteghayyer -> SHENASE','tarifeShenaseyeMoteghayyer',1,'p_tarifeShenaseyeMoteghayyer_1','yacc.py',123),
  ('tarifeShenaseyeMoteghayyer -> SHENASE OPEN_BRACKET INT CLOSE_BRACKET','tarifeShenaseyeMoteghayyer',4,'p_tarifeShenaseyeMoteghayyer_2','yacc.py',128),
  ('tarifeShenaseyeMoteghayyer -> SHENASE OPEN_BRACKET FLOAT CLOSE_BRACKET','tarifeShenaseyeMoteghayyer',4,'p_tarifeShenaseyeMoteghayyer_3','yacc.py',133),
  ('tarifeTabe -> jens SHENASE OPEN_PAREN vorudi CLOSE_PAREN jomle','tarifeTabe',6,'p_tarifeTabe_1','yacc.py',138),
  ('tarifeTabe -> SHENASE OPEN_PAREN vorudi CLOSE_PAREN jomle','tarifeTabe',5,'p_tarifeTabe_2','yacc.py',143),
  ('vorudi -> vorudiha','vorudi',1,'p_vorudi_1','yacc.py',148),
  ('vorudi -> epsilon','vorudi',1,'p_vorudi_2','yacc.py',153),
  ('vorudiha -> vorudiha NOGHTE_VIRGUL jensVorudiha','vorudiha',3,'p_vorudiha_1','yacc.py',158),
  ('vorudiha -> jensVorudiha','vorudiha',1,'p_vorudiha_2','yacc.py',163),
  ('jensVorudiha -> jens shenaseyeVorudiha','jensVorudiha',2,'p_jensVorudiha','yacc.py',168),
  ('shenaseyeVorudiha -> shenaseyeVorudiha COMMA shenaseyeVorudi','shenaseyeVorudiha',3,'p_shenaseyeVorudiha_1','yacc.py',173),
  ('shenaseyeVorudiha -> shenaseyeVorudi','shenaseyeVorudiha',1,'p_shenaseyeVorudiha_2','yacc.py',178),
  ('shenaseyeVorudi -> SHENASE','shenaseyeVorudi',1,'p_shenaseyeVorudi_1','yacc.py',183),
  ('shenaseyeVorudi -> SHENASE OPEN_BRACKET CLOSE_BRACKET','shenaseyeVorudi',3,'p_shenaseyeVorudi_2','yacc.py',188),
  ('jomle -> jomleyeMorakkab','jomle',1,'p_jomle_1','yacc.py',193),
  ('jomle -> jomleyeEbarat','jomle',1,'p_jomle_2','yacc.py',198),
  ('jomle -> jomleyeEntekhab','jomle',1,'p_jomle_3','yacc.py',203),
  ('jomle -> jomleyeTekrar','jomle',1,'p_jomle_4','yacc.py',208),
  ('jomle -> jomleyeBazgasht','jomle',1,'p_jomle_5','yacc.py',213),
  ('jomle -> jomleyeShekast','jomle',1,'p_jomle_6','yacc.py',218),
  ('jomleyeMorakkab -> OPEN_BRACE tarifhayeMahalli jomleha CLOSE_BRACE','jomleyeMorakkab',4,'p_jomleyeMorakkab','yacc.py',223),
  ('jomleha -> jomleha jomle','jomleha',2,'p_jomleha_1','yacc.py',228),
  ('jomleha -> epsilon','jomleha',1,'p_jomleha_2','yacc.py',233),
  ('jomleyeEbarat -> ebarat NOGHTE_VIRGUL','jomleyeEbarat',2,'p_jomleyeEbarat_1','yacc.py',238),
  ('jomleyeEbarat -> NOGHTE_VIRGUL','jomleyeEbarat',1,'p_jomleyeEbarat_2','yacc.py',243),
  ('jomleyeEntekhab -> IF_KW ebarateSade THEN_KW jomle','jomleyeEntekhab',4,'p_jomleyeEntekhab_1','yacc.py',248),
  ('jomleyeEntekhab -> IF_KW ebarateSade THEN_KW jomle ELSE_KW jomle','jomleyeEntekhab',6,'p_jomleyeEntekhab_2','yacc.py',253),
  ('jomleyeEntekhab -> SWITCH_KW OPEN_PAREN ebarateSade CLOSE_PAREN onsoreHalat onsorePishfarz END_KW','jomleyeEntekhab',7,'p_jomleyeEntekhab_3','yacc.py',258),
  ('onsoreHalat -> CASE_KW INT COLON jomle NOGHTE_VIRGUL','onsoreHalat',5,'p_onsoreHalat_1','yacc.py',264),
  ('onsoreHalat -> CASE_KW FLOAT COLON jomle NOGHTE_VIRGUL','onsoreHalat',5,'p_onsoreHalat_2','yacc.py',269),
  ('onsoreHalat -> onsoreHalat CASE_KW INT COLON jomle NOGHTE_VIRGUL','onsoreHalat',6,'p_onsoreHalat_3','yacc.py',274),
  ('onsoreHalat -> onsoreHalat CASE_KW FLOAT COLON jomle NOGHTE_VIRGUL','onsoreHalat',6,'p_onsoreHalat_4','yacc.py',279),
  ('onsorePishfarz -> DEFAULT_KW COLON jomle NOGHTE_VIRGUL','onsorePishfarz',4,'p_onsorePishfarz_1','yacc.py',284),
  ('onsorePishfarz -> epsilon','onsorePishfarz',1,'p_onsorePishfarz_2','yacc.py',289),
  ('jomleyeTekrar -> WHILE_KW OPEN_PAREN ebarateSade CLOSE_PAREN jomle','jomleyeTekrar',5,'p_jomleyeTekrar','yacc.py',294),
  ('jomleyeBazgasht -> RETURN_KW NOGHTE_VIRGUL','jomleyeBazgasht',2,'p_jomleyeBazgasht_1','yacc.py',299),
  ('jomleyeBazgasht -> RETURN_KW ebarat NOGHTE_VIRGUL','jomleyeBazgasht',3,'p_jomleyeBazgasht_2','yacc.py',304),
  ('jomleyeShekast -> BREAK_KW NOGHTE_VIRGUL','jomleyeShekast',2,'p_jomleyeShekast','yacc.py',309),
  ('ebarat -> taghirpazir EQUALS ebarat','ebarat',3,'p_ebarat_1','yacc.py',314),
  ('ebarat -> taghirpazir PLUS_EQ ebarat','ebarat',3,'p_ebarat_2','yacc.py',319),
  ('ebarat -> taghirpazir MINUS_EQ ebarat','ebarat',3,'p_ebarat_3','yacc.py',324),
  ('ebarat -> taghirpazir TIMES_EQ ebarat','ebarat',3,'p_ebarat_4','yacc.py',329),
  ('ebarat -> taghirpazir DIVIDE_EQ ebarat','ebarat',3,'p_ebarat_5','yacc.py',334),
  ('ebarat -> taghirpazir PLUS_PLUS','ebarat',2,'p_ebarat_6','yacc.py',339),
  ('ebarat -> taghirpazir MINUS_MINUS','ebarat',2,'p_ebarat_7','yacc.py',344),
  ('ebarat -> ebarateSade','ebarat',1,'p_ebarat_8','yacc.py',349),
  ('ebarateSade -> ebarateSade OR_KW ebarateSade','ebarateSade',3,'p_ebarateSade_1','yacc.py',354),
  ('ebarateSade -> ebarateSade AND_KW ebarateSade','ebarateSade',3,'p_ebarateSade_2','yacc.py',359),
  ('ebarateSade -> ebarateSade SHORT_CIRCUIT_OR_KW ebarateSade','ebarateSade',3,'p_ebarateSade_3','yacc.py',364),
  ('ebarateSade -> ebarateSade SHORT_CIRCUIT_AND_KW ebarateSade','ebarateSade',3,'p_ebarateSade_4','yacc.py',369),
  ('ebarateSade -> NOT_KW ebarateSade','ebarateSade',2,'p_ebarateSade_5','yacc.py',374),
  ('ebarateSade -> ebarateRabetei','ebarateSade',1,'p_ebarateSade_6','yacc.py',379),
  ('ebarateRabetei -> ebarateRiaziManteghi','ebarateRabetei',1,'p_ebarateRabetei_1','yacc.py',384),
  ('ebarateRabetei -> ebarateRiaziManteghi amalgareRabetei ebarateRiaziManteghi','ebarateRabetei',3,'p_ebarateRabetei_2','yacc.py',389),
  ('amalgareRabetei -> LT','amalgareRabetei',1,'p_amalgareRabetei_1','yacc.py',394),
  ('amalgareRabetei -> GT','amalgareRabetei',1,'p_amalgareRabetei_2','yacc.py',399),
  ('amalgareRabetei -> GE','amalgareRabetei',1,'p_amalgareRabetei_3','yacc.py',404),
  ('amalgareRabetei -> LE','amalgareRabetei',1,'p_amalgareRabetei_4','yacc.py',409),
  ('amalgareRabetei -> EQ','amalgareRabetei',1,'p_amalgareRabetei_5','yacc.py',414),
  ('ebarateRiaziManteghi -> ebarateYegani','ebarateRiaziManteghi',1,'p_ebarateRiaziManteghi_1','yacc.py',419),
  ('ebarateRiaziManteghi -> ebarateRiaziManteghi amalgareRiazi ebarateRiaziManteghi','ebarateRiaziManteghi',3,'p_ebarateRiaziManteghi_2','yacc.py',424),
  ('amalgareRiazi -> PLUS','amalgareRiazi',1,'p_amalgareRiazi_1','yacc.py',429),
  ('amalgareRiazi -> MINUS','amalgareRiazi',1,'p_amalgareRiazi_2','yacc.py',434),
  ('amalgareRiazi -> TIMES','amalgareRiazi',1,'p_amalgareRiazi_3','yacc.py',439),
  ('amalgareRiazi -> DIVIDE','amalgareRiazi',1,'p_amalgareRiazi_4','yacc.py',444),
  ('amalgareRiazi -> MOD','amalgareRiazi',1,'p_amalgareRiazi_5','yacc.py',449),
  ('ebarateYegani -> amalgareYegani ebarateYegani','ebarateYegani',2,'p_ebarateYegani_1','yacc.py',454),
  ('ebarateYegani -> amel','ebarateYegani',1,'p_ebarateYegani_2','yacc.py',459),
  ('amalgareYegani -> MINUS','amalgareYegani',1,'p_amalgareYegani_1','yacc.py',464),
  ('amalgareYegani -> TIMES','amalgareYegani',1,'p_amalgareYegani_2','yacc.py',469),
  ('amalgareYegani -> QUESTION_MARK','amalgareYegani',1,'p_amalgareYegani_3','yacc.py',474),
  ('amel -> taghirpazir','amel',1,'p_amel_1','yacc.py',479),
  ('amel -> taghirnapazir','amel',1,'p_amel_2','yacc.py',484),
  ('taghirpazir -> SHENASE','taghirpazir',1,'p_taghirpazir_1','yacc.py',489),
  ('taghirpazir -> taghirpazir OPEN_BRACKET ebarat CLOSE_BRACKET','taghirpazir',4,'p_taghirpazir_2','yacc.py',494),
  ('taghirpazir -> taghirpazir DOT SHENASE','taghirpazir',3,'p_taghirpazir_3','yacc.py',499),
  ('taghirnapazir -> OPEN_PAREN ebarat CLOSE_PAREN','taghirnapazir',3,'p_taghirnapazir_1','yacc.py',504),
  ('taghirnapazir -> sedaZadan','taghirnapazir',1,'p_taghirnapazir_2','yacc.py',509),
  ('taghirnapazir -> meghdareSabet','taghirnapazir',1,'p_taghirnapazir_3','yacc.py',514),
  ('sedaZadan -> SHENASE OPEN_PAREN bordareVorudi CLOSE_PAREN','sedaZadan',4,'p_sedaZadan','yacc.py',519),
  ('bordareVorudi -> bordareVorudiha','bordareVorudi',1,'p_bordareVorudi_1','yacc.py',524),
  ('bordareVorudi -> epsilon','bordareVorudi',1,'p_bordareVorudi_2','yacc.py',529),
  ('bordareVorudiha -> bordareVorudiha COMMA ebarat','bordareVorudiha',3,'p_bordareVorudiha_1','yacc.py',534),
  ('bordareVorudiha -> ebarat','bordareVorudiha',1,'p_bordareVorudiha_2','yacc.py',539),
  ('meghdareSabet -> INT','meghdareSabet',1,'p_meghdareSabet_1','yacc.py',544),
  ('meghdareSabet -> FLOAT','meghdareSabet',1,'p_meghdareSabet_2','yacc.py',549),
  ('meghdareSabet -> HARFE_SABET','meghdareSabet',1,'p_meghdareSabet_3','yacc.py',554),
  ('meghdareSabet -> TRUE_KW','meghdareSabet',1,'p_meghdareSabet_4','yacc.py',559),
  ('meghdareSabet -> FALSE_KW','meghdareSabet',1,'p_meghdareSabet_5','yacc.py',564),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','yacc.py',569),
]
