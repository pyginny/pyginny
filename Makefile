EXECUTABLE=pyginny
LOG_FILE=/var/log/${EXECUTABLE}.log
PACKAGE=github.com/pyginny/pyginny

.DEFAULT_GOAL := help

help:
	@echo "Type: make [rule]. Available options are:"
	@echo ""
	@echo "- help"
	@echo ""
	@echo "- install"
	@echo "- install-user"
	@echo "- install-p3"
	@echo "- install-user-p3"
	@echo ""
	@echo "- test"
	@echo "- test-cov"
	@echo "- test-on-docker"
	@echo "- test-cov-on-docker"
	@echo ""
	@echo "- deps"
	@echo "- clear"
	@echo "- format"
	@echo ""
	@echo "- pip-package"
	@echo "- pip-upload"
	@echo "- pip-all"
	@echo ""

install:
	pip install -e .[test]

install-user:
	pip install -e .[test] --user

install-p3:
	pip3 install -e .[test]

install-user-p3:
	pip3 install -e .[test] --user

test:
	python setup.py test

test-cov:
	python setup.py test --codecoverage=html

test-on-docker:
	docker run -it --rm -v "${PWD}":/app -w /app python:2.7.14-jessie make deps install test

test-cov-on-docker:
	docker run -it --rm -v "${PWD}":/app -w /app python:2.7.14-jessie make deps install test-cov

deps:
	pip install -r requirements.txt

clear:
	find . -name "*.pyc" -exec rm -f {} \;
	find . -type d -name __pycache__ -exec rm -r {} \+
	rm -rf htmlcov
	rm -rf dist
	rm -rf pyginny.egg-info
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf .coverage*
	rm -rf out

format:
	black .

pip-package:
	python setup.py sdist

pip-upload:
	twine upload dist/*

pip-all:
	make clear
	make pip-package
	make pip-upload

upload:
	rm -rf .git
	git init
	git add .
	git commit -m "initial commit"
	git remote add origin git@github.com:pyginny/pyginny.git
	git push -u --force origin master

backup:
	rm -rf ~/Dropbox/Docs/PRSOLUCOES/pyginny/code
	cp -R ~/Developer/workspaces/python/pyginny ~/Dropbox/Docs/PRSOLUCOES/pyginny/code

sample:
	@rm -rf out
	@pyginny \
		generate \
		extras/examples/records.ginny \
		--java-out=out \
		--java-package=com.pyginny.sample

djinni-sample:
	@rm -rf out
	@"${DJINNI_HOME}/src/run" \
            --java-out "out/java" \
            --java-package com.pyginny.test \
            --java-generate-interfaces true \
            --java-implement-android-os-parcelable true \
            --java-nullable-annotation "javax.annotation.CheckForNull" \
            --java-nonnull-annotation "javax.annotation.Nonnull" \
            --java-use-final-for-record false \
            --ident-java-field mFooBar \
            \
            --cpp-out "out/cpp" \
            --cpp-namespace com.pyginny.test \
            --ident-cpp-enum-type foo_bar \
            --cpp-optional-template "std::experimental::optional" \
            --cpp-optional-header "\"../../handwritten-src/cpp/optional.hpp\"" \
            --cpp-extended-record-include-prefix "../../handwritten-src/cpp/" \
            --cpp-use-wide-strings true \
            \
            --jni-out "out/jni" \
            --ident-jni-class NativeFooBar \
            --ident-jni-file NativeFooBar \
            \
            --objc-out "out/objc" \
            --objcpp-out "out/objc" \
            --objc-type-prefix DB \
            \
            --yaml-out "out/yaml" \
            --yaml-out-file "yaml-test.yaml" \
            --yaml-prefix "test_" \
            \
            --idl "extras/examples/records.ginny"
