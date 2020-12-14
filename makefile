default: test

test:
	python -m unittest tests/test.py

build:
	python3 setup.py sdist bdist_wheel

deploy: build
	twine upload --repository testpypi dist/*
