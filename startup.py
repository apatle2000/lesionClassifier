#work in progress 

# This code is to execite the code easily, if this doesnt work go and start the backend and front end seprately

# libraries imports
import os
from sys import platform
from multiprocessing import Process


def frontEndRunner(self, *args, **kwargs):
    """Function to run the frontend server """
    if platform == "linux" or platform == "linux2":
        # linux
        pass

    if platform == "darwin":
        # OS X
        os.system("cd frontend/lesions \nnpm start ")

    if platform == "win32":
        # Windows...
        pass


def backEndRunner():
    """Function to run the backend server """
    if platform == "linux" or platform == "linux2":
        # linux
        pass
    
    if platform == "darwin":
        # OS X
        os.system("source venv/bin/activate")
        os.system("cd backend/lesionclassifier \npython3 manage.py runserver 8000")

    if platform == "win32":
        # Windows...
        pass

if __name__ == "__main__":

    # basePath = os.path.dirname(os.path.realpath(__file__))
    # print (basePath)
    p1 = Process(target=backEndRunner, args=(''))
    p2 = Process(target=frontEndRunner, args=(""))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("process terminated")
