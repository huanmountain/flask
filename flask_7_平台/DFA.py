# -*- coding:utf-8 -*-
# import requests
#encoding=utf-8
import sys
sys.path.append("../")
import jieba
import time
time1=time.time()

# DFA算法()
class DFAFilter():
    def __init__(self):
        self.keyword_chains = {}
        self.delimit = '\x00'

    def add(self, keyword):
        keyword = keyword.lower()
        chars = keyword.strip()
        if not chars:
            return
        level = self.keyword_chains
        for i in range(len(chars)):
            if chars[i] in level:
                level = level[chars[i]]
            else:
                if not isinstance(level, dict):
                    break
                for j in range(i, len(chars)):
                    level[chars[j]] = {}
                    last_level, last_char = level, chars[j]
                    level = level[chars[j]]
                last_level[last_char] = {self.delimit: 0}
                break
        if i == len(chars) - 1:
            level[self.delimit] = 0

    def parse(self, path):
        with open(path,encoding='utf-8') as f:
            for keyword in f:
                self.add(str(keyword).strip())

    def filter(self, message, repl="*"):
        message = message.lower()
        ret = []
        start = 0
        while start < len(message):
            level = self.keyword_chains
            step_ins = 0
            for char in message[start:]:
                if char in level:
                    step_ins += 1
                    if self.delimit not in level[char]:
                        level = level[char]
                    else:
                        ret.append(repl * step_ins)
                        start += step_ins - 1
                        break
                else:
                    ret.append(message[start])
                    break
            else:
                ret.append(message[start])
            start += 1

        return ''.join(ret)


def cuttest(test_sent,path=None):
    # result1 = str(jieba.cut(test_sent))
    # result = DFA.MaskSen(result1)
    # print(" ".join(result))
    if path is None:
        path = "static/Sensitive/my.txt"
    cut_list = jieba.cut(test_sent)
    cut_str = " ".join(cut_list)
    cut_str_list = cut_str.split(" ")
    cuter = ""
    # 如果整个单词都是敏感词就屏蔽，否则不屏蔽
    for i in cut_str_list:
        # 记录初始值
        init_value = i
        i = MaskSen(i,path)
        flag = 0
        # 判断是否都为**，
        for j in i:
            if j != '*':
                flag = 1
                break
        if flag == 0:
            cuter = cuter + i
        else:
            cuter = cuter + init_value
    return cuter




def cut_deal(test_sent,path=None):
    # result1 = str(jieba.cut(test_sent))
    # result = DFA.MaskSen(result1)
    # print(" ".join(result))
    if path is None:
        path = "static/Sensitive/my.txt"
    cut_list = jieba.cut(test_sent)
    cut_str = "/".join(cut_list)
    cut_str_list = cut_str.split(" ")
    return cut_str


def MaskSen(word,path):
    gfw = DFAFilter()
    gfw.parse(path)
    # #text= input("input:")
    # text = word
    return gfw.filter(word)
    # print(text)
    # print(result)
    # time2 = time.time()
    # print('总共耗时：' + str(time2 - time1) + 's')

# if __name__ == "__main__":
#     path= "Sensitive/sensitive_my.txt"
#     text="中国人民大学川纯我爱你人民上美食"
#     print(cuttest(text,path))



