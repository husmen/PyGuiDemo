# Requirements
- Conda
- PIP
    - PySide6
    - opencv-python
    - pyinstaller 

# How to
```
conda create -n qt python=3.9
conda activate qt
pip install -r requirements.txt
pyinstaller.exe .\main.py -F -w
./dist/main.exe
```

# More info
- [Qt for Python - Documentation](https://doc.qt.io/qtforpython/)
- [Trajectory-Mapping (PyQt5 app)](https://github.com/husmen/Trajectory-Mapping)
- [QuadTree (Qt5 C++ app)](https://github.com/husmen/QuadTree)