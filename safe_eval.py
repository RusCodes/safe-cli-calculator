import ast
import operator as op

# Mapping AST op nodes to functions
BIN_OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
}
UNARY_OPS = {
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}

def _eval(node):
    """
    Recursively evaluates a valid AST node.
    """
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float, complex)):
            return node.value
        raise ValueError("Only numeric constants are allowed.")
    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        op_type = type(node.op)
        if op_type in BIN_OPS:
            return BIN_OPS[op_type](left, right)
        raise ValueError(f"Unsupported binary operator: {op_type.__name__}")
    if isinstance(node, ast.UnaryOp):
        operand = _eval(node.operand)
        op_type = type(node.op)
        if op_type in UNARY_OPS:
            return UNARY_OPS[op_type](operand)
        raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
    
    # Catch-all for any other node types, preventing malicious code.
    raise ValueError(f"Unsupported expression type: {node.__class__.__name__}")

def safe_eval(expr):
    """
    Parses and safely evaluates a string expression.
    """
    try:
        # The 'eval' mode is crucial to parse expressions, not statements
        parsed = ast.parse(expr, mode='eval')
        return _eval(parsed)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")

def main():
    """
    Main function to run the CLI or REPL.
    """
    import sys
    
    if len(sys.argv) > 1:
        # CLI Mode: Evaluate the expression from command-line arguments.
        expr = " ".join(sys.argv[1:])
        try:
            result = safe_eval(expr)
            print(result)
        except ValueError as e:
            print(f"Error: {e}")
    else:
        # REPL Mode: Start an interactive loop.
        print("Safe Calculator REPL. Press Ctrl-C or Ctrl-D to exit.")
        while True:
            try:
                s = input("calc> ")
                if not s.strip():
                    continue
                result = safe_eval(s)
                print(f"=> {result}")
            except (EOFError, KeyboardInterrupt):
                print("\nExiting.")
                break
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()