from collections import OrderedDict

from classes.result import Create, Result, Update, Delete


class JsonDiff:
    def __init__(self) -> None:
        self.results: list[Result] = []

    def json_diff(self, j1, j2, context: str = ""):
        if type(j1) is not type(j2):
            pass
        else:
            if isinstance(j1, dict):
                j1 = OrderedDict(sorted(j1.items()))
                j2 = OrderedDict(sorted(j2.items()))
                set_keys_j1 = set(j1.keys())
                set_keys_j2 = set(j2.keys())
                intersection = set_keys_j1 & set_keys_j2
                for i in intersection:
                    self.json_diff(j1[i], j2[i], f"{context}/{i}")
                for lo in set_keys_j1 - intersection:
                    self.results.append(Delete(context, lo, j1[lo]))
                for ro in set_keys_j2 - intersection:
                    self.results.append(Create(context, ro, j2[ro]))
            elif isinstance(j1, list):
                left_only, right_only = self.list_diff(j1, j2)
                if left_only and right_only:
                    self.check_lists_update(left_only, right_only, context)
                    return
                for n, lo in enumerate(left_only):
                    self.results.append(Delete(context, n, lo))
                for n, ro in enumerate(right_only):
                    self.results.append(Create(context, n, ro))
            else:
                if j1 != j2:
                    self.results.append(Update(context, None, f"{j1} -> {j2}"))

    def check_lists_update(self, left_only, right_only, context: str):
        if len(left_only) == len(right_only):
            for n, (j1, j2) in enumerate(zip(left_only, right_only)):
                self.json_diff(j1, j2, f"{context}/{n}")
        else:
            min_len = min(len(left_only), len(right_only))
            for n in range(min_len):
                self.json_diff(left_only[n], right_only[n], f"{context}/{n}")
            if min_len == len(left_only):
                for n in range(min_len, len(right_only)):
                    self.results.append(Create(context, n, right_only[n]))
            else:
                for n in range(min_len, len(left_only)):
                    self.results.append(Delete(context, n, left_only[n]))

    def list_diff(self, list1, list2):
        intersection = [obj for obj in list1 if obj in list2 and obj in list1]
        left_diff = [obj for obj in list1 if obj not in intersection]
        right_diff = [obj for obj in list2 if obj not in intersection]
        if left_diff or right_diff:
            return left_diff, right_diff
        return [], []
