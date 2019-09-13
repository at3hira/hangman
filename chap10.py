"""
ハングマンゲーム（単語当てゲーム）
　回答者が１文字ずつ文字を入力して、最終的に単語を当てる。
　単語に含まれていない文字を入力した場合、変数stagesの絵を１パーツ毎表示する。
　最終的に絵が全て表示されたら負け、絵が表示される前に単語を当てられたら勝ち。

word : 答える単語
wrong : 間違った回数
rletters : 答えを１文字ずつ分けたリスト。答えなければならない残りの文字を記憶させておく
bord : rlettersと同様のリスト。回答者に見せるヒント用

"""
import random

def hangman(word):
    wrong = 0 
    stages = ["",
              "_______    ",
              "|          ",
              "|      |   ",
              "|      o   ",
              "|     /|\  ",
              "|     / \  ",
              "|          "   
    ]
    rletters = list(word)
    # 最初は文字数分アンダースコアを表示させる
    bord = ["_"] * len(word) 
    win = False
    print("ハングマン、スタート")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字入力してください。"
        char = input(msg)
        # 正解
        if char in rletters:
            char_index = rletters.index(char)
            # 変数bordは回答者に表示させるのでindex値を使って正しい文字に置き換え
            bord[char_index] = char
            # 変数rlettersは正解した文字を$マークに置き換える。同じ文字が複数あった場合indexメソッドが正常に動作しないため
            rletters[char_index] = '$'
        # 不正解
        else:
            wrong += 1
        
        print(" " .join(bord))
        e = wrong + 1
        print("\n" .join(stages[0:e]))
        if "_" not in bord:
            print("あなたの勝ちです")
            print(" " .join(bord))
            win = True
            break
    if not win:
        print("\n" .join(stages[0:wrong + 1]))
        print("あなたの負けです")
        print("正解は {}." .format(word))


characters = ["captainamerica",
              "ironman",
              "hulk",
              "hawkeye",
              "thor",
]
list_index = random.randint(0,4) # index値をランダムで生成
answer = characters[list_index]

hangman(answer)
