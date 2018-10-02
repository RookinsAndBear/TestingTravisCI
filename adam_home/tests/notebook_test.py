import subprocess
import tempfile
import os
import nbformat
import json

# https://blog.thedataincubator.com/2016/06/testing-jupyter-notebooks/
def _exec_notebook(path):
    ''' 
        Execute a jupyter notebook vis nbconvert and collect the output.
        
        returns:    parsed nb object
                    execution errors
    '''
    
    # dirname, __ = os.path.split(path)
    # os.chdir(dirname)
    # convert *.ipynb from jupyter notebook to py notebook
    # "--ExecutePreprocessor.allow_errors=TRUE",
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=120",
                "--output", fout.name, path]
        # submodule allows you to spawn new processes, connect to their input/
        # output/error pipes, and obtain their return codes.
        subprocess.check_call(args)
        # seek() sets the file's current position.
        fout.seek(0)
        # https://www.reddit.com/r/learnpython/comments/4qa46k/json_object_must_be_str_not_bytes/
        # py3 uses bytes natively and the json parser can't handle it, convert to a string first.
        byte2str = fout.read().decode('utf-8')
        file2str = json.loads(byte2str)
        # https://nbformat.readthedocs.io/en/latest/api.html
        nb = nbformat.read(file2str, nbformat.current_nbformat) #TypeError
        
        # https://nbformat.readthedocs.io/en/latest/format_description.html
        # nb = nbformat.read(fout, as_version=4)
        
    # errors = [output for cell in nb.cells if "outputs" in cell
    #            for output in cell["outputs"]\
    #          if output.output_type == "error"]
    
    return 0 # nb, errors
        

def test():
    # nb, errors = _notebook_run('/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos/example.ipynb')
    r_val = _exec_notebook('/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos/example.ipynb')
    assert errors == []
    # _exec_notebook('/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos/example.ipynb')
    # _exec_notebook('/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos/Orbit_Period_Uncertainty_Trending_demo.ipynb') 
