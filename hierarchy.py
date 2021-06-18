import collections
import json
from collections import defaultdict

# def group(rows):
#     return {}


# def ungroup(hierarchy):
#     return []


lst = [["one", "two", "three", "four"], [
    "one", "two", "three", "five"], [1, 2, 3, 4], [1, 2, 3, 6]]


def group(rows):

    tree = {}
    result = {}
    for item in rows:
        # last_2nd_ele = item[len(item) - 2]
        # last_element = item[len(item) - 1]
        currTree = tree
        for key in item[::]:
            if key not in currTree:
            
                currTree[key] = {}
                currTree = currTree[key]
            print(tree, "tree :")
    # print(result, "result")


group(lst)

  # print("result", result1)
    # breakpoint()
    # res = {}
    # d1 = [tree]
    # print(d1, "etg")
    # breakpoint()
    # for dict in d1:
    #     for list in dict:
    #         if list in res:
    #             res[list] += (dict[list])
    #         else:
    #             res[list] = dict[list]
    # print("new tree", tree)
    # dictA = tree
    # result = {}
    # final_op = {}
    # for k, v in dictA.items():
    #     for nk, nv in v.items():
    #         if result.__contains__(nk):
    #             i = 0
    #             while i < len(result[nk]):
    #                 result[nk][i] += nv[i]
    #                 i += 1
    #         else:
    #             result[nk] = nv
    # final_op = result
    # print(final_op)

        # for i in range(len(rows)-1):
                #     print(rows[i])
                #     if item == rows[i+1]:
                #         result = defaultdict(list)
                #         result = tree
                #         for k, v in currTree.items():
                #             for k1, v1, in v.items():
                #                 print(v, "v")
                #                 print(k1, "k1")
                #                 print(v1, "v1")
                #                 if key == k1:
                # result.setdefault(k1, []).append(v1)
                # print("888888888")
                # result[k1].append(v1)
                # result[k1].append(v1)
                # if key, currTree[i] not in currTree:
                #     print(i, "jh")
                # if key == last_2nd_ele:
                    # currTree[key] = [last_element]
                    # pass
            # else:
            #     if key != last_element: