import subprocess
import tempfile
import nbformat
import os
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError

def _exec_notebook(path):
    ''' 
        Execute a jupyter notebook via nbconvert.
    '''
    # print("exec notebookt path passed in: ", path)
    # print("exec notebook os.getcwd: ", os.getcwd())
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert",
                "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=120",
                "--ExecutePreprocessor.kernel_name=python3",
                #"--output", fout.name , path]
                "--output", os.getcwd() + "/temp102218" , path]
        print(" ".join(args))
        subprocess.check_call(args)
    return
        
# https://blog.thedataincubator.com/2016/06/testing-jupyter-notebooks/
def _process_notebook(path):
    ''' 
        Execute a jupyter notebook via nbconvert and collect the output.
        
        returns:    parsed nb object
                    execution errors
    '''
    # in_file = '/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos/Orbit_Period_Uncertainty_Trending_demo.ipynb'
    # dirname, in_file = os.path.split(path)
    # print("process notebookt path passed in: ", path)
    # print("process notebook os.getcwd: ", os.getcwd())
    #os.chdir(dirname)
    # convert *.ipynb from jupyter notebook to py notebook
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert",
                "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=120",
                "--ExecutePreprocessor.kernel_name=python3",
                #"--output", fout.name , path]
                "--output", os.getcwd() + "/temp110518" , path]
        # submodule allows you to spawn new processes, connect to their input/
        # output/error pipes, and obtain their return codes.
        # print(" ".join(args))
        subprocess.check_call(args)
        # seek() sets the file's current position.
        fout.seek(0)
        nb = nbformat.read(os.getcwd() + "/temp110518.ipynb", nbformat.current_nbformat)

    #errors = [output for cell in nb.cells if "outputs" in cell
    #            for output in cell["outputs"]\
    #            if output.output_type == "AssertionError"]

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
    print(cwd)
    # local
    # notebook_path = cwd + '/PublicAppVeyor/tests/example.ipynb'
    # appveyor
    os.chdir("..")
    testdir = os.getcwd()
    notebook_path = testdir + '/tests/example.ipynb'
    #_exec_notebook(notebook_path)
    nb, errors = _process_notebook(notebook_path)

    # assert that errors is empty, otherwise fail
    # assert errors == []
    # assert that errors is 0, otherwise fail
    assert errors == 0, 'Executed Notebook Returned with ERRORS'

def main():
    test()


if __name__ == "__main__":
    main()
