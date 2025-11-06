import os
class PrintAllFilesInCurrentDirectory:
    """
    This class contains a method to print all files in the current directory.
    """

    @staticmethod
    def print_all_files():
        for entry in os.listdir('.'):
            if os.path.isfile(os.path.join('.', entry)):
                print(entry)


# Example usage
if __name__ == "__main__":
    printer = PrintAllFilesInCurrentDirectory()
    printer.print_all_files()