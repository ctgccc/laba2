def process_argument(arg):
    if isinstance(arg, list):
        arg = [x for x in arg if x >= 0]
        if 0 in arg:
            idx = arg.index(0)
            arg = arg[idx+1:]
        return sum(arg)
    elif isinstance(arg, tuple):
        arg = list(arg)
        return (max(arg), min(arg))
    elif isinstance(arg, int):
        return sum(int(x) for x in str(arg) if int(x) % 2 != 0)
    elif isinstance(arg, str):
        words = arg.split()
        return len([word for word in words if len(word) % 2 == 0])
    else:
        return "Неверный тип аргумента"
