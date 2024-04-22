# Tabela de transições do automato
tabela = [#   0   1   2  3  4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23                                           
          #  chm chM dig .  "   #   >   <   =   /   &   %   *   +   ~   -   (   )   :    x  _   e   \n  " "
            [36, 28, 1,  21,32, 66, 43, 42, 41, 65, 64, 63, 62, 60, 59, 55, 71, 73, 75, -1, -1, 36, -1, -1], #estado 0
            [-1, -1, 2,  4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 26, -1, 29, -1, -1, 26, 26], #estado 1
            [-1, -1, 3,  4, -1, -1, -1, -1, -1, 5,  -1, -1, -1, -1, -1, -1, -1, 26, -1, -1, 6,  -1, 26, 26], #estado 2 
            [-1, -1, 27, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 26, -1, -1, -1, -1, 26, 26], #estado 3
            [-1, -1, 21, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 25, -1, -1, -1, 22, 25, 25], #estado 4
            [-1, -1, 7,  -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 5
            [-1, -1, 9,  -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 6   
            [-1, -1, 8,  -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 7        
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, 12, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 8        
            [-1, -1, 10, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 9
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1], #estado 10
            [-1, -1, 13, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 11
            [-1, -1, 13, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 12           
            [-1, -1, 14, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 13
            [-1, -1, 15, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 14
            [-1, -1, 18, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 15
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 16 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 17 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 16, -1, -1, -1, -1, 16, 16], #estado 18 
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 19 (NULO)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 20 (NULO)
          #  chm chM dig .  "   #   >   <   =   /   &   %   *   +   ~   -   (   )   :    x  _   e   \n  " "
            [-1, -1, 21, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 25, -1, -1, -1, 35, 25, 25], #estado 21
            [-1, -1, 24, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 23, -1, -1, -1, -1, -1, -1, -1, -1], #estado 22
            [-1, -1, 24, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 23
            [-1, -1, 24, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 25, 25, -1, -1, -1, 25, 25], #estado 24
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 25 (Aceita)  
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 26 (Aceita) 
            [-1, -1, 27, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 26, 26], #estado 27
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 29, -1, -1, -1, -1], #estado 28
            [-1, 30, 30, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 29
            [-1, 30, 30, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 31, -1, -1, -1, -1, 31, 31], #estado 30 
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 31 (Aceita)            
            [33, 33, 33, 33,33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, -1, 33], #estado 32   
            [33, 33, 33, 33,34, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, 33, -1, 33], #estado 33    
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 34 (Aceita)
            [-1, -1, 24, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 23, -1, -1, -1, -1, -1, -1, -1, -1], #estado 35 
            [83, 37, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 83, -1, 83, -1, -1], #estado 36 
            [38, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 39, -1, -1, -1, 38, 39, 39], #estado 37
            [-1, 37, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 39, -1, 37, -1, -1, 39, 39], #estado 38  
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 39 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 40 (Aceita)
            [40, 40, 40, 40,40, 40, 40, 40, 44, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40], #estado 41   
            [-1, -1, -1, -1,-1, -1, 49, 76, 46, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 45, 45], #estado 42         
            [-1, -1, -1, -1,-1, -1, -1, -1, 57, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 58, 58], #estado 43
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 44 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 45 (Aceita)
            [47, 47, 47, 47,47, 47, 47, 47, 48, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47, 47], #estado 46
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 47 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 48 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 49 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 50 (NULO)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 51 (NULO)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 52 (NULO)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 53 (NULO)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 54 (NULO)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 55 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 56 (NULO)  
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 57 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 58 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 59 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 60 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 61 (NULO)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 62 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 63 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 64 (Aceita)
          #  chm chM dig .  "   #   >   <   =   /   &   %   *   +   ~   -   (   )   :    x  _   e   \n  " "
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 65 (Aceita)
            [67, 67, 67, 67,67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 17, 67], #estado 66 
            [67, 67, 67, 67,67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 17, 67], #estado 67
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 68 (NULO)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 69 (NULO)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 70 (NULO)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 71 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 72 (NULO)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 73 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 74 (NULO)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 75 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, 77, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 76
            [78, 78, 78, 78,78, 78, 78, -1, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78], #estado 77
            [78, 78, 78, 78,78, 78, 79, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78, 78], #estado 78
            [-1, -1, -1, -1,-1, -1, 80, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 79
            [-1, -1, -1, -1,-1, -1, 81, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 80
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 81 (Aceita)
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 82 (NULO)
            [83, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 84, -1, -1, 83, 83, 83, 84, 84], #estado 83
            [-1, -1, -1, -1,-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1], #estado 84 (Aceita)
          ]

# lista de estados de aceitação
estados_aceitacao = [16, 17, 25, 26, 31, 34, 39, 40, 44, 45, 47, 49, 55, 57, 58, 59, 60, 62, 63, 64, 65, 71, 73, 75, 81, 84, 48]

# lista de estados de aceitação para cadeias que não precisam de um caractere fora do escopo do seu token para gerar o token
estados_aceitacao_independentes = [34, 44, 49, 55, 57, 59, 60, 62, 63, 64, 65, 71, 73, 75, 81, 48]

# Lista de tokens possíveis
tokens = [
          'tk_data',              # 16
          'tk_comentariolinha',   # 17
          'tk_float',             # 25
          'tk_int',               # 26
          'tk_end',               # 31
          'tk_cadeia',            # 34
          'tk_id',                # 39
          'tk_=',                 # 40
          'tk_==',                # 44
          'tk_<',                 # 45
          'tk_<=',                # 47
          'tk_<>',                # 49
          'tk_-',                 # 55
          'tk_>=',                # 57
          'tk_>',                 # 58
          'tk_~',                 # 59
          'tk_+',                 # 60
          'tk_*',                 # 62
          'tk_%',                 # 63
          'tk_&',                 # 64
          'tk_/',                 # 65
          'tk_(',                 # 71
          'tk_)',                 # 73
          'tk_:',                 # 75
          'tk_comentariobloco',   # 81
          'tk_palavrareservada',  # 84
          'tk_<==',               # 48
        ]

# Lista de caracteres reconhecidos pela linguagem
possiveis_caracteres = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z', # letras minusculas/coluna = 0
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', # LETRAS MAIUSCULAS/coluna = 1
                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', # Numeros/coluna = 2
                        '.', '"', '#', '>', '<', '=', '/', '&', '%', '*', '+', '~', '-', '(', ')', ':', 'x', '_', 'e', '\n',' ', '']

# Palavras reservadas da linguagem
palavras_reservadas = ['rotina', 'fim_rotina', 'se', 'senao', 'imprima', 'leia', 'para', 'enquanto']

# Tokens de palavras reservadas
tokens_cadeias_reservadas = ['tk_rotina', 'tk_fim_rotina', 'tk_se', 'tk_senao', 'tk_imprima', 'tk_leia', 'tk_para', 'tk_enquanto']

# Verifica o tipo de caractere lido, retornando o indice da lista de caracteres possiveis correspondente
def verifica_caractere(caractere):
    if caractere in possiveis_caracteres:
        return possiveis_caracteres.index(caractere)
    else:
        return -1

# Verifica o proximo estado do automato, considerando o estado atual e o tipo do caractere que foi lido do arquivo.
def verifica_proximo_estado(estado_atual, tipo_caractere):
    # Cara tipo de caractere está relacionado a uma coluna da tabela de transições acima.
    if 0 <= tipo_caractere <= 23: # Se o caractere lido for do tipo letra minuscula (chm)
        coluna = 0
    elif 24 <= tipo_caractere <= 49: # Se o caractere lido for do tipo letra maiuscula (chM)
        coluna = 1
    elif 50 <= tipo_caractere <= 59: # Se o caractere lido for do tipo digito (dig)
        coluna = 2
    else: # Se o caractere lido for dos outros tipos (que não são intervalos). Os tipos estão estão especificados nos comentários da tabela de transições acima.
        if tipo_caractere == 60:
            coluna = 3
        elif tipo_caractere == 61:
            coluna = 4
        elif tipo_caractere == 62:
            coluna = 5
        elif tipo_caractere == 63:
            coluna = 6
        elif tipo_caractere == 64:
            coluna = 7
        elif tipo_caractere == 65:
            coluna = 8
        elif tipo_caractere == 66:
            coluna = 9
        elif tipo_caractere == 67:
            coluna = 10
        elif tipo_caractere == 68:
            coluna = 11
        elif tipo_caractere == 69:
            coluna = 12
        elif tipo_caractere == 70:
            coluna = 13
        elif tipo_caractere == 71:
            coluna = 14
        elif tipo_caractere == 72:
            coluna = 15
        elif tipo_caractere == 73:
            coluna = 16
        elif tipo_caractere == 74:
            coluna = 17
        elif tipo_caractere == 75:
            coluna = 18
        elif tipo_caractere == 76:
            coluna = 19
        elif tipo_caractere == 77:
            coluna = 20
        elif tipo_caractere == 78:
            coluna = 21
        elif tipo_caractere == 79:
            coluna = 22
        else:
            coluna = 23
        
    # print("Linha: " + str(estado_atual) + " | coluna: " + str(coluna)) # Print para vizualizar o estado atual (Linha da tabela) e a coluna da tabela    
    novo_estado = tabela[estado_atual][coluna] # novo estado receberá o novo estado a partir da posição da tabela
    return novo_estado

def adiciona_colunas_em_lista_tokens(quant_todos_tokens): # Adiciona coluna a lista de quantidade de tokens possiveis (copia da lista tokens)
    quantidade_tokens_inicial = 0 # Atribui o valor inicial da nova coluna em todas as linhas
    tabela = [[string, quantidade_tokens_inicial] for string in quant_todos_tokens] # Cria uma tabela que contem a nova coluna adicionada à lista
    
    return tabela

def contar_ocorrencias(tokens, tokens_gerados):# Conta ocorrencias de um token na lista de tokens gerados
    for token in tokens:
        token[1] = tokens_gerados.count(token[0]) # Atribui o numero de ocorrencias ao respectivo token
    return tokens

def ordenar_quantidade_tokens(tokens): # Ordena tabela de ocorrencia de tokens em ordem decrescente
    tokens.sort(key=lambda token: token[1], reverse=True)
    return tokens

def imprimir_arquivo_saida(arqv, linha): # Imprime texto em um arquivo
    with open(arqv, "a") as arquivo:
        arquivo.write(linha)
        
def limpar_arquivo_saida(arqv): # Limpa conteudo de um arquivo
    with open(arqv, 'w') as arquivo:
        pass

def copiar_conteudo_para_saida_erro(arquivo_entrada, arquivo_saida): # Copia conteudo do arquivo entrada pra o arquivo saida de erros adicionando o numero da linha no inicio de cada linha
    with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
        i = 0
        for linha in entrada: # Formata a impressão do indice para que não desalinhe as colunas do arquivo
            if i <= 9:
                saida.write('[' + str(i) + ' ] ' + linha)
            else:
                saida.write('[' + str(i) + '] ' + linha)
            i+=1

def adicionar_erros(arquivo_saida, tabela_erros):  # Define a função para adicionar mensagens de erro no arquivo de saída.
    with open(arquivo_saida, 'r') as saida:  # Abre o arquivo de saída para leitura.
        linhas = saida.readlines()  # Lê todas as linhas do arquivo e armazena numa lista.

    erros_por_linha = {}  # Cria um dicionário para mapear erros às suas respectivas linhas.
    for linha_erro, coluna_erro in tabela_erros:  # Itera sobre cada par de linha e coluna de erro na tabela de erros.
        if linha_erro not in erros_por_linha:  # Verifica se a linha atual ainda não está no dicionário.
            erros_por_linha[linha_erro] = []  # Inicializa uma lista vazia para os erros dessa linha.
        erros_por_linha[linha_erro].append(coluna_erro)  # Adiciona o erro (coluna) à lista da linha correspondente.
    
    for linha_erro, colunas_erro in erros_por_linha.items():  # Itera sobre cada linha e seus erros no dicionário.
        # Cria a mensagem de erro, indicando a linha e as colunas dos erros, e anexa ao final da linha correspondente.
        mensagem_erros = " |--> Erro na linha: " + str(linha_erro) + " colunas: " + ', '.join([str(coluna) for coluna in colunas_erro]) + ' | (contagem de colunas inicia em 0)'
        linhas[linha_erro] = linhas[linha_erro].rstrip('\n') + mensagem_erros + "\n"  # Anexa a mensagem de erro à linha, removendo qualquer quebra de linha existente antes de adicionar a mensagem de erro e uma nova quebra de linha.
    
    with open(arquivo_saida, 'w') as saida:  # Abre o arquivo de saída para escrita, substituindo o conteúdo existente.
        saida.writelines(linhas)  # Escreve a lista atualizada de linhas de volta ao arquivo de saída.

def main():
    arqv = 'entrada.txt'
    
    with open(arqv, 'r') as arquivo: # Lê e atribui todo o conteudo do arquivo entrada para 'conteudo'
        conteudo = arquivo.read()
    tamanho_arquivo = len(conteudo) # Salva o tamanho do arquivo para identificar futuramente o fim do arquivo

    # Reseta os arquivos de saída
    limpar_arquivo_saida('saida_tokens_gerados.txt')
    limpar_arquivo_saida('saida_ocorrencias_tokens.txt')
    limpar_arquivo_saida('saida_erros.txt')
    
    # Inicializa elementos importantes que seram utilizados
    estado_atual = 0 
    cadeia_atual = ''
    tokens_gerados = []
    tabela_erros = [] 
    erro_encontrado = False
    token_valido = True
    token_gerado_aux = ''
    cont_posicao_arquivo = 0
    index_linha_arquivo = -1
    index_coluna_arquivo_aux = 0
    
    with open(arqv, 'r') as arquivo: # Abre novamente o arquivo de entrada
        for linha in arquivo: # Para cada linha no arquivo...
            
            print('==========================================================================') # Marcador visual para delimitar a linha
            
            index_linha_arquivo += 1 # Incrementa o indice da linha que está sendo lida
            index_coluna_arquivo = -1 # Inicializa (ou reseta) o indice da coluna da linha que está sendo lida
            for caractere in linha: # Para cada caractere na linha atual que está sendo lida ...
                cont_posicao_arquivo += 1 # Incrementa posição global do arquivo (importante para identificar o final do arquivo)
                
                print('-----------------------------------------') # Marcador visual para delimitar a coluna
                # print('POSICAO ARQUIVO: ' + str(cont_posicao_arquivo) + '\n' + 'TAMANHO ARQUIVO: ' + str(tamanho_arquivo)) # Mostra posição global atual em comparação a posição final do arquivo
                print(caractere) # Mostra o caractere atual que está sendo lido
                
                cadeia_atual = cadeia_atual + str(caractere) # Salva caractere em uma cadeia
                tipo_caractere = verifica_caractere(caractere) # Verifica o tipo do caractere em relação a tabela de transições
                
                print('Tipo caractere: ' + str(tipo_caractere)) # Mostra o tipo de caractere atual
                
                estado_aux = estado_atual # Salva o estado atual
                estado_novo = verifica_proximo_estado(estado_atual, tipo_caractere) # Verifica e atribui o proximo estado ao ler o caractere atual
                estado_atual = estado_novo # Atribui à estado atual o proximo estado
                
                if estado_aux == 78 and tipo_caractere == 79:
                    index_coluna_arquivo_aux = index_coluna_arquivo
                
                print('Estado atual: ' + str(estado_aux))
                print('Proximo estado: ' + str(estado_novo))
            
                if estado_atual in estados_aceitacao: # Se o estado que fomos ao ler o caractere for um estado de aceitação da lista de estados de aceitação acima...
                    token_gerado = tokens[estados_aceitacao.index(estado_atual)] # ... então, é gerado o token correspondente à aquele estado de aceitação (os indices das duas listas de tokens e estados de aceitação são correspondentes)
                    token_gerado_aux = token_gerado
                    if token_gerado == tokens[25]: # Caso o token gerado tenha sido de palavra reservada
                        cadeia_atual_aux = cadeia_atual[:-1]
                        print( 'PALAVRA RESERVADA: ' + cadeia_atual_aux )
                        if cadeia_atual_aux in palavras_reservadas: # Verifica se a cadeia está na lista de palavras reservadas
                            index_palavra_reservada = palavras_reservadas.index(cadeia_atual_aux)
                            token_gerado = tokens_cadeias_reservadas[index_palavra_reservada] # Gera o token para a palavra reservada específica
                            if tipo_caractere == 73:
                                cadeia_atual = cadeia_atual_aux
                        else:
                            token_valido = False
                    
                    if token_valido == True:
                        tokens_gerados.append(token_gerado) # O token gerado é atribuido a uma lista de tokens gerados, para ser feito o controle de quantidade de tokens de cada tipo
                        if token_gerado == tokens[24]: # Se o token gerado é o de comentario em bloco
                            if '\n' in cadeia_atual:
                                cadeia_atual_aux = cadeia_atual.split('\n')[0]
                                tamanho_cadeia = len(cadeia_atual_aux)
                                index_cadeia_inicial = (index_coluna_arquivo_aux-1) - (tamanho_cadeia - 1)
                        else:        
                            tamanho_cadeia = len(cadeia_atual) # Salva o tamanho da cadeia
                            index_cadeia_inicial = index_coluna_arquivo - (tamanho_cadeia - 1) # # Salva a coluna do indice inicial da cadeia atual
                        
                        print('Token: ' + token_gerado) # Mostra o token gerado para a cadeia atual após ter lido o caractere que engatilhou a geração do token
                        
                        if (tipo_caractere > 78 or (tipo_caractere == 74 and token_gerado != tokens[22])) and cont_posicao_arquivo < tamanho_arquivo: # Se o caractere que engatilhou a geração do token foi um espaço, ou quebra de linha, ou fechamento de parentese, ele não faz parte da cadeia. Logo, deve ser retirado
                            cadeia_atual = cadeia_atual[:-1] # Retira o ultimo elemento da cadeia, que é o espaço, ou quebra de linha, ou fechamento de parentese
                        
                        # Imprime no arquivo saída o token gerado com sua respectiva cadeia, linha e coluna (coluna onde inicia a cadeia, não onde o token foi gerado. Achei que facilitaria a identificação da cadeia)
                        imprimir_arquivo_saida('saida_tokens_gerados.txt', 'Linha: ' + str(index_linha_arquivo) + ' | Coluna: ' + str(index_cadeia_inicial + 1) + ' | ' + token_gerado + ' |--> ' + str(''.join(cadeia_atual)) + '\n')                        
                        
                        cadeia_atual = '' # Reseta a cadeia atual
                        
                        if token_gerado_aux == tokens[25]: # Se token gerado foi uma palavra reservada
                            if tipo_caractere == 73: # Se caractere foi uma abertura de parentese
                                cadeia_atual = cadeia_atual + str(caractere)
                                estado_atual = verifica_proximo_estado(0, tipo_caractere)
                                if estado_atual in estados_aceitacao:
                                    token_gerado = tokens[estados_aceitacao.index(estado_atual)]
                                    tokens_gerados.append(token_gerado)
                                    imprimir_arquivo_saida('saida_tokens_gerados.txt', 'Linha: ' + str(index_linha_arquivo) + ' | Coluna: ' + str(index_coluna_arquivo) + ' | ' + token_gerado + ' |--> ' + str(''.join(cadeia_atual)) + '\n')
                                cadeia_atual = '' # Reseta a cadeia atual
                                estado_atual = 0
                        else:
                            if (tipo_caractere == 74 or tipo_caractere == 75 ) and estado_atual not in estados_aceitacao_independentes: # Caso o caractere lido seja um fechamento de parentese ou dois pontos e o estado atual não está na lista de estados de aceitação independentes
                                cadeia_atual = cadeia_atual + str(caractere)
                                estado_atual = verifica_proximo_estado(0, tipo_caractere)
                                if estado_atual in estados_aceitacao:
                                    token_gerado = tokens[estados_aceitacao.index(estado_atual)]
                                    tokens_gerados.append(token_gerado)
                                    print('Token: ' + token_gerado)
                                    imprimir_arquivo_saida('saida_tokens_gerados.txt', 'Linha: ' + str(index_linha_arquivo) + ' | Coluna: ' + str(index_coluna_arquivo) + ' | ' + token_gerado + ' |--> ' + str(''.join(cadeia_atual)) + '\n')
                                cadeia_atual = '' # Reseta a cadeia atual
                                estado_atual = 0 # Reseta o automato para o estado 0
                    estado_atual = 0 # Reseta o automato para o estado 0
                        
                    token_valido = True
                elif estado_atual == -1: # Se o estado que fomos ao ler o caractere for um estado de rejeição (representado por -1 na tabela de transições acima)...
                    if tipo_caractere <=78 and erro_encontrado == False: # Se o caractere que engatilhou o estado de rejeição NÃO FOI um espaço ou uma quebra de linha (e caso não tenha sido encontrado nenhum erro anteriormente na cadeia)
                        tabela_erros.append([index_linha_arquivo, index_coluna_arquivo]) # salva linha e coluna do erro encontrado em um registro de erros
                        erro_encontrado = True # status de erro encontrado alterado para True, indicando que o primeiro erro daquela cadeia já foi registrado
                    elif tipo_caractere > 78: # Se o caractere que engatilhou o estado de rejeição FOI um espaço ou uma quebra de linha...
                        if estado_aux not in estados_aceitacao and estado_aux > 0: # Se FOI um espaço ou quebra de linha e o estado anterior ao atual não foi um estado de aceitação nem o estado 0 inicial do automato...
                            tabela_erros.append([index_linha_arquivo, index_coluna_arquivo]) # Salva a linha e a coluna que o erro foi encontrado
                            erro_encontrado = True # Se o caractere que engatilhou o estado de rejeição FOI um espaço ou uma quebra de linha...
                        estado_atual = 0 # Reseta o automato, já que foi lido um espaço ou quebra de linha, que indica o fim de uma cadeia
                        cadeia_atual ='' # Reseta a cadeia atual
                        erro_encontrado = False # Reseta o status de primeiro erro encontrado                    
                elif estado_atual not in estados_aceitacao and estado_atual != -1 and cont_posicao_arquivo == tamanho_arquivo: # Se estado atual não for de aceitação, nem de rejeição e chegamos no FINAL do arquivo...
                    estado_aux = estado_atual # Salva o estado atual
                    estado_novo = verifica_proximo_estado(estado_atual, 81) # Verifica qual proximo estado do automato no caso especifico para fim de arquivo presente na tabela de transições (ultima coluna) 
                    estado_atual = estado_novo # Estado atual recebe proximo estado
                    if estado_atual in estados_aceitacao: # Se o novo estado for aceitação...
                        token_gerado = tokens[estados_aceitacao.index(estado_atual)] #... O token é gerado,
                        if token_gerado == tokens[25]:
                            print( 'PALAVRA RESERVADA: ' + cadeia_atual )
                            if cadeia_atual in palavras_reservadas:
                                index_palavra_reservada = palavras_reservadas.index(cadeia_atual)
                                token_gerado = tokens_cadeias_reservadas[index_palavra_reservada]
                            else:
                                token_valido = False
                        
                        if token_valido == True:
                            tokens_gerados.append(token_gerado) # O token é registrado na lista de tokens gerados
                            
                            print('Token: ' + token_gerado) # Mostra qual o token gerado
                            
                            estado_atual = 0 # Reseta o automato para o estado 0
                            tamanho_cadeia = len(cadeia_atual) # Salva tamanho da cadeia atual
                            index_cadeia_inicial = index_coluna_arquivo - (tamanho_cadeia - 1) # Salva a coluna do indice inicial da cadeia atual
                            # Imprime no arquivo saída o token gerado com sua respectiva cadeia, linha e coluna
                            imprimir_arquivo_saida('saida_tokens_gerados.txt', 'Linha: ' + str(index_linha_arquivo) + ' | Coluna: ' + str(index_cadeia_inicial + 1) + ' | ' +token_gerado + ' |--> ' + str(''.join(cadeia_atual)) + '\n')
                            cadeia_atual = '' # Reseta cadeia atual
                            
                        token_valido = True
                    else: # Se o novo estado não for aceitação...
                        tabela_erros.append([index_linha_arquivo, index_coluna_arquivo]) # Registra linha e coluna do erro
                index_coluna_arquivo += 1 # Incrementa o indice da coluna que está sendo lida
    
    quant_todos_tokens = []
    quant_todos_tokens = tokens # Cria copia da lista de tokens possiveis de serem gerados
    quant_todos_tokens.pop()
    quant_todos_tokens.extend(tokens_cadeias_reservadas)
    quant_todos_tokens = adiciona_colunas_em_lista_tokens(quant_todos_tokens) # Adiciona coluna na lista, tornando-a uma tabela
    quant_todos_tokens = contar_ocorrencias(quant_todos_tokens, tokens_gerados) # Conta quantas vezes cada tipo de token aparece na tabela e atribui o valor ao respectivo token
    quant_todos_tokens = ordenar_quantidade_tokens(quant_todos_tokens) # Ordena tabela em ordem decrescente de ocorrências
    
    # Impressão de arquivo de ocorrencias de tokens
    for linha in quant_todos_tokens: # Para cada linha da tabela de ocorrencia de tokens...
        linha_formatada = f"{linha[0]} |--> {linha[1]}" # ... É aplicada uma formatação
        if linha[1] > 0: # Se a ocorrencia for maior que 0...
            imprimir_arquivo_saida('saida_ocorrencias_tokens.txt', linha_formatada + '\n') # ... A linha é impressa no arquivo
            
    copiar_conteudo_para_saida_erro(arqv, 'saida_erros.txt') # Copia o conteudo do arquivo de entrada para o arquivo saida de erros, onde, caso existam, serão mostrados
    adicionar_erros('saida_erros.txt', tabela_erros) # Modifica o arquivo saida de erros, que possui a copia do arquivo de entrada, adicionando mensagens de erro que indicam a linha e a coluna que o erro foi encontrado
    
main()