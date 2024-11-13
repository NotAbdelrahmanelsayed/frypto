rm -rf dist/ build/ *.egg-info
python -m build
# python -m twine upload --repository testpypi dist/*
twine upload dist/*