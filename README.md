# Step-by-step guide
1. Run `python3 -m build` in the source directory.
2. Run `python3 -m venv venv` to create a virtual environment.
3. Activate your virtual environment:
- `source venv/bin/activate` for UNIX.
- `.\venv\Scripts\activate` for Windows.
4. Install the package `pip install dist/test_project-1.0.0-py3-none-any.whl`.
5. Run `python3 -m test_project` or simply `test_demo`. This might take a while.