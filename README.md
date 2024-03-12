# Build from source
Run `python3 -m build` in the source directory.

# Step-by-step installation guide
1. Run `python3 -m venv venv` to create a virtual environment.
2. Activate your virtual environment:
   - `source venv/bin/activate` for UNIX.
   - `.\venv\Scripts\activate` for Windows.
3.
   1. Install the package and its main dependencies, one of:
      - `poetry install`
      - `pip install dist/test_project-1.0.0-py3-none-any.whl`
      - `pip install git+https://github.com/Dimignat/hse-mcv-dist-project`

   2. To additionally install development dependencies, one of:
      - `poetry install -E dev`
      - `pip install 'dist/test_project-1.0.0-py3-none-any.whl[dev]'`
      - `pip install -e git+https://github.com/Dimignat/hse-mcv-dist-project#egg=project[dev]`

4. Run `python3 -m test_project` or simply `test_demo`. This might take a while.
