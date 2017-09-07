# -*- coding: utf-8 -*-
# 解决列表中输出中文乱码问题。只适用于Python2
import json
lists = ["one", "two", "three", "four", "five"]
print(lists[0])

lists[0] = "six"
print(lists)
lists.append("别闹，我才是萌新！")
print(json.dumps(lists, encoding="utf-8", ensure_ascii=False))
