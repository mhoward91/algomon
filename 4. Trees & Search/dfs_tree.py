# Trees are acyclic, always with a path from root to any node
# Has n - 1 edges, n = num of nodes in tree
# Each node has ONE parent node (except the root node)
# Internal nodes are all nodes but the leaf nodes (including the root)

# Binary tree: every node has no more than 2 children
# Full binary tree: every node has 0 or 2 children
# Complete: All levels filled (except maybe last), nodes far left as poss
# Perfect: All internal nodes have 2 children, leaf nodes same level
#   nodes = 2^n - 1, where n is number of levels
#   internal nodes = num leaf nodes - 1
#   total nodes = 2 * num leaf nodes - 1

# TRAVERSALS
# in order - visits left, current node, right
# pre-order - visits current node, left, right
# post-order - visits left, right, current node

# STRATEGY
# determine return value to pass value from child to parent (max depth, node)
# determine states to pass down in function calls to children (parent value)
# in this example, state is the target node, which also return value if found
def dfs_bin_tree(root, target):
    if root is None:
        return
    if root.val == target:
        return root
    return dfs_bin_tree(root.left, target) or dfs_bin_tree(root.right, target)


def max_depth_bin_tree(root) -> int:
    def dfs(root):
        if not root:
            return 0

        return max(dfs(root.left), dfs(root.right)) + 1

    return dfs(root) - 1 if root else 0
