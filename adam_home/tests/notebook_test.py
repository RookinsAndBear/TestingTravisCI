import subprocess
import tempfile
import nbformat
import os
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError
import sys

def _process_notebook(path):

    ''' 
        Execute a jupyter notebook via nbconvert and collect the output.
        returns:    parsed nb object

                    execution errors
    '''

    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:

        args = ["jupyter", "nbconvert",
                "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=120",
                "--ExecutePreprocessor.kernel_name=python3",
                #"--output", fout.name , path]
                "--output", os.getcwd() + "/temp031819" , path]
        subprocess.check_call(args)
        fout.seek(0)
        nb = nbformat.read(os.getcwd() + "/temp031819.ipynb", nbformat.current_nbformat)



    stream_type = [output for cell in nb.cells if "outputs" in cell
                for output in cell["outputs"]\
                if output.output_type == "stream"]

    errors = 0

    for i in stream_type:
        make_str = str(i)
        # use doctest for unique string or set string message with unittest
        if '***Test Failed***' in make_str: 
            errors = 1
            # print(i)

    return nb, errors


def test():

    cwd = os.getcwd()
    print("Current working dir: ", cwd) 
    #Current working dir:  /home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos
    os.chdir("..")
    testdir = os.getcwd()
    print("Test directory (go up 1 level): ", testdir)
    #Test directory (go up 1 level):  /home/travis/build/RookinsAndBear/TestingTravisCI/adam_home
    print(sys.path)

    # TEST STKWrapper_withDocstring.ipynb
    notebook_path = cwd + '/STKWrapper_withDocstring_workingCopy.ipynb'
    nb, errors_wrapper = _process_notebook(notebook_path)
    # assert that errors is 0, otherwise fail
    assert errors_wrapper == 0, 'Executed Notebook Returned with ERRORS'

    # TEST KariScience_withSTKWrapper.ipynb
    notebook_path = testdir + '/tests/KariScience_withSTKWrapper.ipynb'
    nb, errors_wrapper = _process_notebook(notebook_path)
    # assert that errors is 0, otherwise fail
    assert errors_wrapper == 0, 'Executed Notebook Returned with ERRORS'

    # TEST example.ipynb
    notebook_path = testdir + '/tests/example.ipynb'
    nb, errors_example = _process_notebook(notebook_path)
    # assert that errors is 0, otherwise fail
    assert errors_example == 0, 'Executed Notebook Returned with ERRORS'


def main():
    test()


if __name__ == "__main__":
    main() 
