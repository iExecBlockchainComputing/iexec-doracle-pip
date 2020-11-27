.PHONY: build

build:
	python3 setup.py sdist bdist_wheel

publish:
	python3 -m twine upload --repository testpypi dist/*

clean:
	rm -rf build dist iexec_doracle.egg-info
