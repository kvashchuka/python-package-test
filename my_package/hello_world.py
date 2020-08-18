
def print_hello(st: str = None):
    """

    :param st:
    :return:
    """
    if st is not None:
        print("Hello, {}!".format(st))
    else:
        print("Hello world!")


class HelloPrinter:

    def __init__(self):
        """

        """
        pass
