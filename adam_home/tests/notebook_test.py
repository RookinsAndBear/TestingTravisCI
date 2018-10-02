import subprocess
import tempfile
# import os
# import nbformat

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
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=120",
                "--output", fout.name, path]
        # submodule allows you to spawn new processes, connect to their input/
        # output/error pipes, and obtain their return codes.
        subprocess.check_call(args)
        # seek() sets the file's current position.
        # fout.seek(0)
        
        # https://nbformat.readthedocs.io/en/latest/api.html
        # nb = nbformat.read(fout, nbformat.current_nbformat)
        
    # errors = [output for cell in nb.cells if "outputs" in cell
    #            for output in cell["outputs"]\
    #            if output.output_type == "error"]
    
    # return nb, errors
        

def test():
    _exec_notebook('/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos/example.ipynb')
    # _exec_notebook('/home/travis/build/RookinsAndBear/TestingTravisCI/adam_home/demos/Orbit_Period_Uncertainty_Trending_demo.ipynb') 
