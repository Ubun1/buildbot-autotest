clean-pyc:
	find . -name '*.pyc' -exec rm --force {} \;
	find . -name '*.pyo' -exec rm --force {} \;
	find . -name '*~' -exec rm --force {}  \;

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

clean: clean-pyc clean-build

.PHONY: clean clean-pyc clean-build
