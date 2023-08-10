#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def is_anagram(p1, p2):
    if len(p1) == len(p2):
        ordem1 = sorted(p1)
        ordem2 = sorted(p2)
        return ordem1 == ordem2
    return False





# Teste a sua função aqui (caso ache necessário)











