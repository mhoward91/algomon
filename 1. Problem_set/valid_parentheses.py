# time O(n), space O(n) or O(1) if sorting is considered in place &
# disregarded (it often is)
def valid_parentheses(s: str) -> bool:
    stack = list()
    pairs = {"()", "[]", "{}"}
    for char in s:
        if char in "([{":
            stack.append(char)
        elif not stack or stack.pop() + char not in pairs:
            return False

    return not stack
