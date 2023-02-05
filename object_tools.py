from .output import printer

output = printer.print

output("..imported object tools")


def inspect(obj):
    """Print all things relevant to an object."""
    output("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for i in dir(obj):
        output(f"{i} :: {getattr(obj,i)}")
    try:
        for i in obj:
            output(f"ITEM: {i}")
    except:
        output("not a list")
    try:
        for i in obj.keys():
            output(f"{i} :: {obj[i]}")
    except:
        output("not a dict")
    output("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
