# Placeholder for testing.
# Currently unused.
#
# coverage:
#	rm -rf pdlscraper/cover
#	rm -rf .coverage
#	nosetests -w pdlscraper \
#		--cover-package=pdlscraper \
#		--cover-html \
#		--with-coverage \
#		--cover-inclusive \
#		--cover-erase

lint:
	flake8 pdlscraper
