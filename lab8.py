"""
Justin Hahn
Lab8- Objects

***Note statistical abbreviations
ftm=Free throws made
fta= Free throws attempted
ftp=Free throw percentage
"""


class Basketball():
    """get the free throw percentage of a basektball player"""

    def __init__(self, ftm, fta):
        self.__ftm = ftm
        self.__fta = fta
        self.__ftp = 0

    def get_ftm(self):
        return self.__ftm

    def get_fta(self):
        return self.__fta

    def set_ftp(self, ftp):
        self.__ftp = ftm / fta

    """Setter function"""

    def get_ftp(self):
        return self.__ftp

    """Getter function"""


def main():
    ftm = input("Enter made free throws by a player")
    fta = input("Enter total attempted free throws by a player")
    ftp = "???"
    print("The players free throw percentage is", Basketball(ftm, fta).get_ftp())


if __name__ == "__main__":
    main()
