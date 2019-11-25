python setup.py sdist
@echo off
set /p version="Enter version number: "
twine upload dist/*%version%*